#!/usr/bin/env python3

from __future__ import annotations

import json
from functools import cached_property
from typing import List, Tuple
from urllib.request import getproxies

import requests
from faker import Faker
from requests import Session
from requests.adapters import HTTPAdapter
from requests.models import Response
from urllib3.util.retry import Retry


class RequestHandler(object):
    """
    RequestHandler
    ==============
    Defines a synchronous request handler class as an additional abstraction to
    the `requests` library which uses session objects for working with REST APIs.
    
    Example
    -------
        >>> from lolicon.utils import RequestHandler
        >>> handler = RequestHandler()
        >>> response = handler.get(url=r"https://pokeapi.co/api/v2/pokemon/charizard")
        >>> print(response.ok)
    """
    _timeout = (5, 5)
    _total = 5
    _status_forcelist = [413, 429, 500, 502, 503, 504]
    _backoff_factor = 1
    _fake = Faker()

    def __init__(self, 
                 timeout: Tuple[float, float]=_timeout, 
                 total: int=_total, 
                 status_forcelist: List[int]=_status_forcelist, 
                 backoff_factor: int=_backoff_factor):
        """
        Instantiates a new request handler object.
        """
        self.timeout = timeout
        self.total = total        
        self.status_forcelist = status_forcelist
        self.backoff_factor = backoff_factor

    @cached_property
    def retry_strategy(self) -> Retry:
        """
        The retry strategy returns the retry configuration made up of the
        number of total retries, the status forcelist as well as the backoff
        factor. It is used in the session property where these values are 
        passed to the HTTPAdapter. 
        """
        return Retry(total=self.total,
            status_forcelist=self.status_forcelist,
            backoff_factor=self.backoff_factor
        )

    @cached_property
    def session(self) -> Session:
        """
        Creates a custom session object. A request session provides cookie
        persistence, connection-pooling, and further configuration options
        that are exposed in the RequestHandler methods in form of parameters 
        and keyword arguments.
        """
        assert_status_hook = lambda response, *args, **kwargs: response.raise_for_status()
        session = requests.Session()
        session.mount("https://", HTTPAdapter(max_retries=self.retry_strategy))
        session.hooks['response'] = [assert_status_hook]
        session.headers.update({
            "Content-Type": "application/json; charset=utf-8",
            "User-Agent" : RequestHandler._fake.chrome(version_from=86, version_to=92, build_from=4300, build_to=4400)
        })
        return session
    
    def get(self, url: str, **kwargs) -> Response:
        """
        Returns the GET request encoded in `utf-8`. Adds proxies to this session
        on the fly if urllib is able to pick up the system's proxy settings.
        """
        response = self.session.get(url, timeout=self.timeout, proxies=getproxies(), **kwargs)
        response.encoding = 'utf-8'
        return response

    def post(self, url: str, payload: dict=None, **kwargs) -> Response:
        """
        Returns a `utf-8` encoded POST request. Adds proxies to this session
        on the fly if urllib is able to pick up the system's proxy settings.
        """
        data = json.dumps(payload, ensure_ascii=False).encode('utf-8')
        return self.session.post(url, timeout=self.timeout, data=data, proxies=getproxies(), **kwargs)
