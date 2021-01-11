#!/usr/bin/env python3

from __future__ import annotations

from typing import List, Tuple

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
    def data(self) -> Tuple:
        return utils.query_db(db='elements.db', sql="SELECT * FROM Element WHERE Symbol=?", parameters=(self.symbol,))[0]

    @property
    def name(self) -> str:
        return self.data[1]

    @property
    def atomic_number(self) -> int:
        return self.data[2]

    @property
    def atomic_mass(self) -> Quantity:
        return self.data[3] * utils.UNIT.Da

    @property
    @utils.raise_on_none('atomic_radius')
    def atomic_radius(self) -> Quantity:
        return self.data[4] * utils.UNIT.m

    @property
    def number_of_neutrons(self) -> int:
        return self.data[5]

    @property
    def number_of_protons(self) -> int:
        return self.data[6]

    @property
    def number_of_electrons(self) -> int:
        return self.data[7]

    @property
    def period(self) -> int:
        return self.data[8]

    @property
    def phase(self) -> str:
        return self.data[9]

    @property
    def radioactive(self) -> bool:
        return utils.str_to_bool(self.data[10])
    
    @property
    def natural(self) -> bool:
        return utils.str_to_bool(self.data[11])

    @property
    def metal(self) -> bool:
        return utils.str_to_bool(self.data[12])

    @property
    def metalloid(self) -> bool:
        return utils.str_to_bool(self.data[13])

    @property
    def type(self) -> str:
        return self.data[14]

    @property
    @utils.raise_on_none('electronegativity')
    def electronegativity(self) -> float:
        return self.data[15]
            
    @property
    def first_ionization(self) -> Quantity:
        return self.data[16] * utils.UNIT.eV

    @property
    @utils.raise_on_none('density')
    def density(self) -> Quantity:
        return self.data[17] * 1000 * utils.UNIT.g / (utils.UNIT.cm ** 3)

    @property
    @utils.raise_on_none('melting_point')
    def melting_point(self) -> Quantity:
        return self.data[18] * utils.UNIT.K

    @property
    @utils.raise_on_none('boiling_point')
    def boiling_point(self) -> Quantity:
        return self.data[19] * utils.UNIT.K

    @property
    @utils.raise_on_none('number_of_isotopes')
    def number_of_isotopes(self) -> int:
        return self.data[20]

    @property
    @utils.raise_on_none('specific_heat')
    def specific_heat(self) -> Quantity:
        return self.data[21] * utils.UNIT.J / (utils.UNIT.g * utils.UNIT.K)

    @property
    def number_of_shells(self) -> int:
        return self.data[22]

    @property
    @utils.raise_on_none('number_of_valance')
    def number_of_valance(self) -> int:
        return self.data[23]

    #endregion

    #region methods

    @staticmethod
    def list() -> List[Element]:
        symbols = utils.query_db(db='elements.db', sql="SELECT ? FROM Element", parameters=('Symbol',))
        return [Element(symbol[0]) for symbol in symbols]

    #endregion
    