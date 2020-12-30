#!/usr/bin/env python3

from __future__ import annotations

import math
from typing import List

from pint.quantity import Quantity

from . import utils


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
    def __init__(self, name: str) -> Planet:
        self.name = name.capitalize()

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(ID={self.id})"

    #region operators

    def __gt__(self, other) -> bool:
        return self.id > other.id

    def __ge__(self, other) -> bool:
        return self.id >= other.id

    def __eq__(self, other) -> bool:
        return self.id == other.id

    def __le__(self, other) -> bool:
        return self.id <= other.id

    def __lt__(self, other) -> bool:
        return self.id < other.id

    def __ne__(self, other) -> bool:
        return self.id != other.id

    #endregion

    #region property

    @property
    def data(self) -> dict:
        for planet in utils.load_resource('lolicon.data', 'planets.json'):
            if self.name == planet.get('Name'):
                return planet

    @property
    def id(self) -> int:
        return self.data['ID']

    @property
    def mass(self) -> Quantity:
        """
        This is the mass of the planet in septillion (1 followed by 24 zeros) 
        kilograms or sextillion (1 followed by 21 zeros) tons. Strictly speaking 
        tons are measures of weight, not mass, but are used here to represent 
        the mass of one ton of material under Earth gravity.
        """
        return self.data['Mass'] * math.pow(10, 24) * utils.UNIT.kg

    @property
    def diameter(self) -> Quantity:
        """
        The diameter of the planet at the equator, the distance through the center
        of the planet from one point on the equator to the opposite side, in 
        kilometers or miles.
        """
        return self.data['Diameter'] * utils.UNIT.m

    @property
    def density(self) -> Quantity:
        """
        The average density (mass divided by volume) of the whole planet (not 
        including the atmosphere for the terrestrial planets) in kilograms per 
        cubic meter or pounds per cubic foot.
        """
        return self.data['Density'] * utils.UNIT.kg / (utils.UNIT.m ** 3)

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
        return self.data['Gravity'] * utils.UNIT.m / (utils.UNIT.s ** 2)

    @property
    def escape_velocity(self) -> Quantity:
        """
        Initial velocity, in kilometers per second or miles per second, needed 
        at the surface (at the 1 bar pressure level for the gas giants) to escape 
        the body's gravitational pull, ignoring atmospheric drag.
        """
        return self.data['EscapeVelocity'] * utils.UNIT.km / utils.UNIT.s

    @property
    def rotation_period(self) -> Quantity:
        """
        This is the time it takes for the planet to complete one rotation relative 
        to the fixed background stars (not relative to the Sun) in hours. Negative 
        numbers indicate retrograde (backwards relative to the Earth) rotation.
        """
        return self.data['RotationPeriod'] * utils.UNIT.hour

    @property
    def length_of_day(self) -> Quantity:
        """
        The average time in hours for the Sun to move from the noon position in 
        the sky at a point on the equator back to the same position.
        """
        return self.data['LengthOfDay'] * utils.UNIT.hour

    @property
    def distance_from_sun(self) -> Quantity:
        """
        This is the average distance from the planet to the Sun in millions of 
        kilometers or millions of miles, also known as the semi-major axis. All 
        planets have orbits which are elliptical, not perfectly circular, so 
        there is a point in the orbit at which the planet is closest to the Sun, 
        the perihelion, and a point furthest from the Sun, the aphelion. The 
        average distance from the Sun is midway between these two values. The 
        average distance from the Earth to the Sun is defined as 1 Astronomical 
        Unit (AU), so the ratio table gives this distance in AU.

        For the Moon, the average distance from the Earth is given.
        """
        return self.data['DistanceFromSun'] * math.pow(10, 6) * utils.UNIT.km

    @property
    def perihelion(self) -> Quantity:
        """
        The closest and furthest points in a planet's orbit about the Sun.

        For the Moon, the closest and furthest points to Earth are given, known 
        as the "Perigee" and "Apogee" respectively.
        """
        return self.data['Perihelion'] * math.pow(10, 6) * utils.UNIT.km

    @property
    def aphelion(self) -> Quantity:
        """
        The closest and furthest points in a planet's orbit about the Sun.

        For the Moon, the closest and furthest points to Earth are given, known 
        as the "Perigee" and "Apogee" respectively.
        """
        return self.data['Aphelion'] * math.pow(10, 6) * utils.UNIT.km

    @property
    def orbital_period(self) -> Quantity:
        """
        This is the time in Earth days for a planet to orbit the Sun from one 
        vernal equinox to the next. Also known as the tropical orbit period, 
        this is equal to a year on Earth.

        For the Moon, the sidereal orbit period, the time to orbit once relative 
        to the fixed background stars, is given. The time from full Moon to full 
        Moon, or synodic period, is 29.53 days. For Pluto, the tropical orbit 
        period is not well known, the sidereal orbit period is used.
        """
        return self.data['OrbitalPeriod'] * utils.UNIT.day

    @property
    def orbital_velocity(self) -> Quantity:
        """
        The average velocity or speed of the planet as it orbits the Sun, in 
        kilometers per second or miles per second.

        For the Moon, the average velocity around the Earth is given.
        """
        return self.data['OrbitalVelocity'] * (utils.UNIT.km / utils.UNIT.s)

    @property
    def orbital_inclination(self) -> Quantity:
        """
        The angle in degrees at which a planets orbit around the Sun is tilted 
        relative to the ecliptic plane. The ecliptic plane is defined as the 
        plane containing the Earth's orbit, so the Earth's inclination is 0.
        """
        return self.data['OrbitalInclination'] * utils.UNIT.deg

    @property
    def orbital_eccentricity(self) -> float:
        """
        This is a measure of how far a planet's orbit about the Sun (or the Moon's 
        orbit about the Earth) is from being circular. The larger the eccentricity, 
        the more elongated is the orbit, an eccentricity of 0 means the orbit is a 
        perfect circle. There are no units for eccentricity.
        """
        return self.data['OrbitalEccentricity']

    @property
    def obliquity_to_orbit(self) -> Quantity:
        """
        The angle in degrees the axis of a planet (the imaginary line running 
        through the center of the planet from the north to south poles) is tilted 
        relative to a line perpendicular to the planet's orbit around the Sun, 
        north pole defined by right hand rule.
        
        Venus rotates in a retrograde direction, opposite the other planets, so 
        the tilt is almost 180 degrees, it is considered to be spinning with its 
        "top", or north pole pointing "downward" (southward). Uranus rotates almost 
        on its side relative to the orbit, Pluto is pointing slightly "down". 
        The ratios with Earth refer to the axis without reference to north or south.
        """
        return self.data['ObliquityToOrbit'] * utils.UNIT.deg

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
        return utils.UNIT.Quantity(self.data['MeanTemperature'], utils.UNIT.degC)

    @property
    @utils.raise_on_none('surface_pressure')
    def surface_pressure(self) -> Quantity:
        """
        This is the atmospheric pressure (the weight of the atmosphere per unit area) 
        at the surface of the planet in bars or atmospheres.
        
        The surfaces of Jupiter, Saturn, Uranus, and Neptune are deep in the atmosphere 
        and the location and pressures are not known.
        """
        return self.data['SurfacePressure'] * utils.UNIT.bar

    @property
    def number_of_moons(self) -> int:
        """
        This gives the number of IAU officially confirmed moons orbiting the planet. 
        New moons are still being discovered.
        """
        return self.data['NumberOfMoons']

    @property
    def ring_system(self) -> bool:
        """
        This tells whether a planet has a set of rings around it, Saturn being 
        the most obvious example.
        """
        return self.data['HasRingSystem']

    @property
    def global_magnetic_field(self) -> bool:
        """
        This tells whether the planet has a measurable large-scale magnetic field. 
        Mars and the Moon have localized regional magnetic fields but no global 
        field.
        """
        return self.data['HasGlobalMagneticField']

    #endregion

    #region methods

    @staticmethod
    def list() -> List[Planet]:
        return [Planet(planet['Name']) for planet in utils.load_resource('lolicon.data', 'planets.json')]

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
    def __init__(self, name: str) -> Planet:
        self.name = name.capitalize()

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(ID={self.id})"

    #region operators

    def __gt__(self, other) -> bool:
        return self.id > other.id

    def __ge__(self, other) -> bool:
        return self.id >= other.id

    def __eq__(self, other) -> bool:
        return self.id == other.id

    def __le__(self, other) -> bool:
        return self.id <= other.id

    def __lt__(self, other) -> bool:
        return self.id < other.id

    def __ne__(self, other) -> bool:
        return self.id != other.id

    #endregion

    #region property

    @property
    def data(self) -> dict:
        for satellite in utils.load_resource('lolicon.data', 'satellites.json'):
            if self.name == satellite.get('Name'):
                return satellite

    @property
    def id(self) -> int:
        return self.data['ID']

    @property
    def planet(self) -> Planet:
        """
        Owning planet of the satellite.
        """
        for planet in utils.load_resource('lolicon.data', 'planets.json'):
            if self.data['PlanetID'] == planet.get('ID'):
                return planet

    @property
    def gm(self) -> Quantity:
        return self.data['GM'] * (utils.UNIT.km ** 3) / (utils.UNIT.s ** 2)

    @property
    def radius(self) -> Quantity:
        return self.data['Radius'] * utils.UNIT.km

    @property
    def density(self) -> Quantity:
        return self.data['Density'] * utils.UNIT.g / (utils.UNIT.cm ** 3)

    @property
    def magnitude(self) -> float:
        """
        Apparent Magnitude is the magnitude of an object as it appears in the sky 
        on Earth. Apparent Magnitude is also referred to as Visual Magnitude.
        """
        return self.data['Magnitude']

    @property
    def albedo(self) -> float:
        """
        Geometric albedo is the ratio of a body's brightness at zero phase angle 
        to the brightness of a perfectly diffusing disk with the same position and 
        apparent size as the body.
        """
        return self.data['Albedo']

    #endregion

    #region methods

    @staticmethod
    def list() -> List[Satellite]:
        return [Satellite(satellite['Name']) for satellite in utils.load_resource('lolicon.data', 'satellites.json')]

    #endregion
    