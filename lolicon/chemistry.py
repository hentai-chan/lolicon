#!/usr/bin/env python3

from __future__ import annotations

import functools
import json
from importlib.resources import path as resource_path

import pint
from colorama import Fore
from pint.quantity import Quantity

from . import utils


class Element(object):
    __unit = pint.UnitRegistry()

    def raise_on_none(variable: str):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                try:
                    if func(*args, **kwargs) is None:
                        raise ValueError(f"{Fore.RED}{variable} is None")
                    return func(*args, **kwargs)
                except TypeError:
                    raise ValueError(f"{Fore.RED}{variable} is None")
            return wrapper
        return decorator
    
    def __init__(self, symbol: str) -> Element:
        self.symbol = symbol

    @staticmethod
    def __get_pse_data(symbol: str) -> dict:
        with resource_path('lolicon.data', 'pse.json') as resource_handler:
            with open(resource_handler, 'r', encoding='utf-8') as file_handler:      
                for element in json.load(file_handler)  :
                    if symbol == element['Symbol']:
                        return element

    #region properties

    @property
    def data(self) -> dict:
        return Element.__get_pse_data(self.symbol)

    @property
    def name(self) -> str:
        return self.data['Element']

    @property
    def atomic_number(self) -> int:
        return self.data['AtomicNumber']

    @property
    def atomic_mass(self) -> Quantity:
        return self.data['AtomicMass'] * Element.__unit.Da

    @property
    @raise_on_none('atomic_radius')
    def atomic_radius(self) -> Quantity:
        return self.data['AtomicRadius'] * Element.__unit.m

    @property
    def number_of_neutrons(self) -> int:
        return self.data['NumberOfNeutrons']

    @property
    def number_of_protons(self) -> int:
        return self.data['NumberOfProtons']

    @property
    def number_of_electrons(self) -> int:
        return self.data['NumberOfElectrons']

    @property
    def period(self) -> int:
        return self.data['Period']

    @property
    def phase(self) -> str:
        return self.data['Phase']

    @property
    def radioactive(self) -> bool:
        return self.data['Radioactive']
    
    @property
    def natural(self) -> bool:
        return self.data['Natural']

    @property
    def metal(self) -> bool:
        return self.data['Metal']

    @property
    def metalloid(self) -> bool:
        return self.data['Metalloid']

    @property
    def type(self) -> str:
        return self.data['Type']

    @property
    @raise_on_none('electronegativity')
    def electronegativity(self) -> float:
        return self.data['Electronegativity']
            
    @property
    def first_ionization(self) -> Quantity:
        return self.data['FirstIonization'] * Element.__unit.eV

    @property
    @raise_on_none('density')
    def density(self) -> Quantity:
        unit = Element.__unit.g / (Element.__unit.cm ** 3)
        return self.data['Density'] * 1000 * unit

    @property
    @raise_on_none('melting_point')
    def melting_point(self) -> Quantity:
        return self.data['MeltingPoint'] * Element.__unit.K

    @property
    @raise_on_none('boiling_point')
    def boiling_point(self) -> Quantity:
        return self.data['BoilingPoint'] * Element.__unit.K

    @property
    @raise_on_none('number_of_isotopes')
    def number_of_isotopes(self) -> int:
        return self.data['NumberOfIsotopes']

    @property
    @raise_on_none('specific_heat')
    def specific_heat(self) -> Quantity:
        unit = Element.__unit.J / (Element.__unit.g * Element.__unit.K)
        return self.data['SpecificHeat'] * unit

    @property
    def number_of_shells(self) -> int:
        return self.data['NumberOfShells']

    @property
    @raise_on_none('number_of_valance')
    def number_of_valance(self) -> int:
        return self.data['NumberOfValence']

    #endregion
    