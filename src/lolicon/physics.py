#!/usr/bin/env python3

from __future__ import annotations

import math
from os import name
from typing import List, Tuple

from pint.quantity import Quantity

from . import utils
from .utils import UREG


class Planet(object):
    """
    Planet
    ======

    Basic Usage
    -----------
        >>> from lolicon.physics import Planet
        >>> earth = Planet('earth')
        >>> print(earth.diameter)
        12756 meter

    This interface exposes planetary data from the NASA Jet Propulsion Laboratory
    as `pint` quantities. See reference data sheet at <https://nssdc.gsfc.nasa.gov/planetary/factsheet/planetfact_notes.html>
    """
    def __init__(self, name: str, local_: bool=False) -> Planet:
        """
        Instantiate a new planet from the solar system.
        """
        self.__name = name.capitalize()
        self.__local = local_

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(Name={self.name})"

    #region operators

    def __eq__(self, other) -> bool:
        return self.name == other.name

    def __ne__(self, other) -> bool:
        return self.name != other.name

    #endregion

    #region property

    @property
    def __data(self) -> Tuple:
        return utils.query_db('planets.db', "SELECT * FROM Planet WHERE Name=?", (self.name,), local_=self.__local)[0]

    @property
    def name(self) -> str:
        """
        Return the English name of this planet.
        """
        return self.__name

    @property
    def mass(self) -> Quantity:
        """
        This is the mass of the planet in septillion (1 followed by 24 zeros)
        kilograms.
        """
        return self.__data[1] * math.pow(10, 24) * UREG.kg

    @property
    def diameter(self) -> Quantity:
        """
        The diameter of the planet at the equator, the distance through the center
        of the planet from one point on the equator to the opposite side, in kilometers.
        """
        return self.__data[2] * UREG.km

    @property
    def density(self) -> Quantity:
        """
        The average density (mass divided by volume) of the whole planet (not
        including the atmosphere for the terrestrial planets) in kilograms per
        cubic meter.
        """
        return self.__data[3] * UREG.kg / (UREG.m ** 3)

    @property
    def gravity(self) -> Quantity:
        """
        The gravitational acceleration on the surface at the equator in meters
        per second squared or feet per second squared, including the effects of
        rotation. For the gas giant planets the gravity is given at the 1 bar
        pressure level in the atmosphere. The gravity on Earth is designated as
        1 "G", so the Earth ratio fact sheets gives the gravity of the other
        planets in G's.
        """
        return self.__data[4] * UREG.m / (UREG.s ** 2)

    @property
    def escape_velocity(self) -> Quantity:
        """
        Initial velocity, in kilometers per second, needed at the surface (at
        the 1 bar pressure level for the gas giants) to escape the body's
        gravitational pull, ignoring atmospheric drag.
        """
        return self.__data[5] * UREG.km / UREG.s

    @property
    def rotation_period(self) -> Quantity:
        """
        This is the time it takes for the planet to complete one rotation relative
        to the fixed background stars (not relative to the Sun) in hours. Negative
        numbers indicate retrograde (backwards relative to the Earth) rotation.
        """
        return self.__data[6] * UREG.hour

    @property
    def length_of_day(self) -> Quantity:
        """
        The average time in hours for the Sun to move from the noon position in
        the sky at a point on the equator back to the same position.
        """
        return self.__data[7] * UREG.hour

    @property
    def distance_from_sun(self) -> Quantity:
        """
        This is the average distance from the planet to the Sun in millions of
        kilometers, also known as the semi-major axis. All planets have orbits
        which are elliptical, not perfectly circular, so there is a point in the
        orbit at which the planet is closest to the Sun, the perihelion, and a
        point furthest from the Sun, the aphelion. The average distance from the
        Sun is midway between these two values. The average distance from the
        Earth to the Sun is defined as 1 Astronomical Unit (AU), so the ratio
        table gives this distance in AU. For the Moon, the average distance from
        the Earth is given.
        """
        return self.__data[8] * math.pow(10, 6) * UREG.km

    @property
    def perihelion(self) -> Quantity:
        """
        The closest and furthest points in a planet's orbit about the Sun. For
        the Moon, the closest and furthest points to Earth are given, known as
        the "Perigee" and "Apogee" respectively.
        """
        return self.__data[9] * math.pow(10, 6) * UREG.km

    @property
    def aphelion(self) -> Quantity:
        """
        The closest and furthest points in a planet's orbit about the Sun. For the
        Moon, the closest and furthest points to Earth are given, known as the
        "Perigee" and "Apogee" respectively.
        """
        return self.__data[10] * math.pow(10, 6) * UREG.km

    @property
    def orbital_period(self) -> Quantity:
        """
        This is the time in Earth days for a planet to orbit the Sun from one
        vernal equinox to the next. Also known as the tropical orbit period,
        this is equal to a year on Earth. For the Moon, the sidereal orbit period,
        the time to orbit once relative to the fixed background stars, is given.
        The time from full Moon to full Moon, or synodic period, is 29.53 days.
        For Pluto, the tropical orbit period is not well known, the sidereal orbit
        period is used.
        """
        return self.__data[11] * UREG.day

    @property
    def orbital_velocity(self) -> Quantity:
        """
        The average velocity or speed of the planet as it orbits the Sun, in 
        kilometers per second. For the Moon, the average velocity around the Earth
        is given.
        """
        return self.__data[12] * (UREG.km / UREG.s)

    @property
    def orbital_inclination(self) -> Quantity:
        """
        The angle in degrees at which a planets orbit around the Sun is tilted
        relative to the ecliptic plane. The ecliptic plane is defined as the
        plane containing the Earth's orbit, so the Earth's inclination is 0.
        """
        return self.__data[13] * UREG.deg

    @property
    def orbital_eccentricity(self) -> float:
        """
        This is a measure of how far a planet's orbit about the Sun (or the Moon's
        orbit about the Earth) is from being circular. The larger the eccentricity,
        the more elongated is the orbit, an eccentricity of 0 means the orbit is a
        perfect circle. There are no units for eccentricity.
        """
        return self.__data[14]

    @property
    def obliquity_to_orbit(self) -> Quantity:
        """
        The angle in degrees the axis of a planet (the imaginary line running
        through the center of the planet from the north to south poles) is tilted
        relative to a line perpendicular to the planet's orbit around the Sun,
        north pole defined by right hand rule. Venus rotates in a retrograde direction,
        opposite the other planets, so the tilt is almost 180 degrees, it is considered
        to be spinning with its "top", or north pole pointing "downward" (southward).
        Uranus rotates almost on its side relative to the orbit, Pluto is pointing
        slightly "down". The ratios with Earth refer to the axis without reference
        to north or south.
        """
        return self.__data[15] * UREG.deg

    @property
    def mean_temperature(self) -> Quantity:
        """
        This is the average temperature over the whole planet's surface (or for
        the gas giants at the one bar level) in degrees C (Celsius or Centigrade)
        or degrees F (Fahrenheit). For Mercury and the Moon, for example, this
        is an average over the sunlit (very hot) and dark (very cold) hemispheres
        and so is not representative of any given region on the planet, and most
        of the surface is quite different from this average value. As with the Earth,
        there will tend to be variations in temperature from the equator to the poles,
        from the day to night sides, and seasonal changes on most of the planets.
        """
        return UREG.Quantity(self.__data[16], UREG.degC)

    @property
    @utils.raise_on_none('surface_pressure')
    def surface_pressure(self) -> Quantity:
        """
        This is the atmospheric pressure (the weight of the atmosphere per unit area)
        at the surface of the planet in bars or atmospheres. The surfaces of Jupiter,
        Saturn, Uranus, and Neptune are deep in the atmosphere and the location and
        pressures are not known.
        """
        return self.__data[17] * UREG.bar

    @property
    def number_of_moons(self) -> int:
        """
        This gives the number of IAU officially confirmed moons orbiting the planet.
        New moons are still being discovered.
        """
        return self.__data[18]

    @property
    def ring_system(self) -> bool:
        """
        This tells whether a planet has a set of rings around it, Saturn being
        the most obvious example.
        """
        return utils.str_to_bool(self.__data[19])

    @property
    @utils.raise_on_none('global_magnetic_field')
    def global_magnetic_field(self) -> bool:
        """
        This tells whether the planet has a measurable large-scale magnetic field.
        Mars and the Moon have localized regional magnetic fields but no global
        field.
        """
        return utils.str_to_bool(self.__data[20])

    #endregion

    #region methods

    @staticmethod
    def list() -> List[Planet]:
        """
        Return a list of all planets from the solar system.
        """
        names = utils.query_db('planets.db', "SELECT ? FROM Planet", ('Name',))
        return [Planet(name[0]) for name in names]

    #endregion

class Satellite(object):
    """
    Satellite
    =========

    Basic Usage
    -----------
        >>> from lolicon.physics import Satellite
        >>> moon = Satellite('Moon')
        >>> print(moon.radius)
        1737.5 kilometer

    This interface exposes planetary data from the NASA Jet Propulsion Laboratory
    as `pint` quantities. See reference data sheet at <https://ssd.jpl.nasa.gov/?sat_phys_par>
    """
    def __init__(self, name: str, local_: bool=False) -> Planet:
        """
        Instantiate a new satellite from the solar system.
        """
        self.__name = name.capitalize()
        self.__local = local_

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(Name={self.name})"

    #region operators

    def __eq__(self, other) -> bool:
        return self.name == other.name

    def __ne__(self, other) -> bool:
        return self.name != other.name

    #endregion

    #region property

    @property
    def __data(self) -> Tuple:
        return utils.query_db('satellites.db', "SELECT * FROM Satellite WHERE Name=?", (self.name,), local_=self.__local)[0]

    @property
    def name(self) -> str:
        """
        Return the English name of this satellite.
        """
        return self.__name

    @property
    def planet(self) -> Planet:
        """
        Owning planet of the satellite.
        """
        return Planet(self.__data[0])

    @property
    def gm(self) -> Quantity:
        """
        The standard gravitational parameter is defined as the product of the
        gravitational constant G and the mass M of the celestial body.
        """
        return self.__data[2] * (UREG.km ** 3) / (UREG.s ** 2)

    @property
    def radius(self) -> Quantity:
        """
        The mean radius of the celestial body, in kilometers.
        """
        return self.__data[3] * UREG.km

    @property
    @utils.raise_on_none('density')
    def density(self) -> Quantity:
        """
        The mean density of the celestial body, in g/cm³.
        """
        return self.__data[4] * UREG.g / (UREG.cm ** 3)

    @property
    @utils.raise_on_none('magnitude')
    def magnitude(self) -> float:
        """
        Apparent Magnitude is the magnitude of an object as it appears in the sky 
        on Earth. Apparent Magnitude is also referred to as Visual Magnitude.
        """
        return self.__data[5]

    @property
    @utils.raise_on_none('albedo')
    def albedo(self) -> float:
        """
        Geometric albedo is the ratio of a body's brightness at zero phase angle 
        to the brightness of a perfectly diffusing disk with the same position and 
        apparent size as the body.
        """
        return self.__data[6]

    #endregion

    #region methods

    @staticmethod
    def list() -> List[Satellite]:
        """
        Return a list of all satellites from the solar system.
        """
        names = utils.query_db('satellites.db', "SELECT ? FROM Satellite", ('Name',))
        return [Satellite(name[0]) for name in names]

    #endregion
    