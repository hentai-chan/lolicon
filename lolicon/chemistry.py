#!/usr/bin/env python3

from __future__ import annotations

from typing import List

from pint.quantity import Quantity

from . import utils


class Element(object):    
    def __init__(self, symbol: str) -> Element:
        self.symbol = symbol.capitalize()

    def __str__(self) -> str:
        return self.symbol

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(AtomicNumber={self.atomic_number})"

    #region operators

    def __gt__(self, other) -> bool:
        return self.atomic_number > other.atomic_number

    def __ge__(self, other) -> bool:
        return self.atomic_number >= other.atomic_number

    def __eq__(self, other) -> bool:
        return self.atomic_number == other.atomic_number

    def __le__(self, other) -> bool:
        return self.atomic_number <= other.atomic_number

    def __lt__(self, other) -> bool:
        return self.atomic_number < other.atomic_number

    def __ne__(self, other) -> bool:
        return self.atomic_number != other.atomic_number

    #endregion
    
    #region properties

    @property
    def data(self) -> dict:
        for element in utils.load_resource('lolicon.data', 'pse.json'):
            if self.symbol == element.get('Symbol'):
                return element

    @property
    def name(self) -> str:
        return self.data['Element']

    @property
    def atomic_number(self) -> int:
        return self.data['AtomicNumber']

    @property
    def atomic_mass(self) -> Quantity:
        return self.data['AtomicMass'] * utils.UNIT.Da

    @property
    @utils.raise_on_none('atomic_radius')
    def atomic_radius(self) -> Quantity:
        return self.data['AtomicRadius'] * utils.UNIT.m

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
    @utils.raise_on_none('electronegativity')
    def electronegativity(self) -> float:
        return self.data['Electronegativity']
            
    @property
    def first_ionization(self) -> Quantity:
        return self.data['FirstIonization'] * utils.UNIT.eV

    @property
    @utils.raise_on_none('density')
    def density(self) -> Quantity:
        return self.data['Density'] * 1000 * utils.UNIT.g / (utils.UNIT.cm ** 3)

    @property
    @utils.raise_on_none('melting_point')
    def melting_point(self) -> Quantity:
        return self.data['MeltingPoint'] * utils.UNIT.K

    @property
    @utils.raise_on_none('boiling_point')
    def boiling_point(self) -> Quantity:
        return self.data['BoilingPoint'] * utils.UNIT.K

    @property
    @utils.raise_on_none('number_of_isotopes')
    def number_of_isotopes(self) -> int:
        return self.data['NumberOfIsotopes']

    @property
    @utils.raise_on_none('specific_heat')
    def specific_heat(self) -> Quantity:
        return self.data['SpecificHeat'] * utils.UNIT.J / (utils.UNIT.g * utils.UNIT.K)

    @property
    def number_of_shells(self) -> int:
        return self.data['NumberOfShells']

    @property
    @utils.raise_on_none('number_of_valance')
    def number_of_valance(self) -> int:
        return self.data['NumberOfValence']

    #endregion

    #region methods

    @staticmethod
    def list() -> List[Element]:
        return [Element(element['Symbol']) for element in utils.load_resource('lolicon.data', 'pse.json')]

    #endregion
    