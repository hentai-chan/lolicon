#!/usr/bin/env python3

from __future__ import annotations

from typing import List, Tuple

from pint.quantity import Quantity

from . import utils
from .utils import UREG


class Element(object):
    """
    Elememt
    =======

    Basic Usage
    -----------
        >>> from lolicon.chemistry import Element
        >>> gold = Element('Au')
        >>> print(gold.number_of_protons)
        79
    """
    def __init__(self, symbol: str, local_: bool=False) -> Element:
        self.__symbol = symbol.capitalize()
        self.__local = local_

    def __str__(self) -> str:
        return self.symbol

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(Name={self.name})"

    #region operators

    def __eq__(self, other) -> bool:
        return self.atomic_number == other.atomic_number

    def __ne__(self, other) -> bool:
        return self.atomic_number != other.atomic_number

    #endregion
    
    #region properties

    @property
    def __data(self) -> Tuple:
        return utils.query_db('elements.db', "SELECT * FROM Element WHERE Symbol=?", (self.symbol,), local_=self.__local)[0]

    @property
    def symbol(self) -> str:
        """
        Return the chemical symbol for this element.
        """
        return self.__symbol

    @property
    def name(self) -> str:
        """
        The English name of this element, e.g. "Gold" or "Oxygen".
        """
        return self.__data[1]

    @property
    def atomic_number(self) -> int:
        """
        The atomic number or proton number of a chemical element is the number of
        protons (and mass number is the sum of protons and neutrons) found in the
        nucleus of every atom of that element. The atomic number uniquely identifies
        a chemical element. It is identical to the charge number of the nucleus. In
        an uncharged atom, the atomic number is also equal to the number of electrons.
        """
        return self.__data[2]

    @property
    def atomic_mass(self) -> Quantity:
        """
        The mass of an atom. Although the SI unit of mass is kilogram, the atomic
        mass is often expressed in the non-SI unit dalton (symbol: Da, or u) where
        1 dalton is defined as ​1⁄12 of the mass of a single carbon-12 atom, at rest.
        The protons and neutrons of the nucleus account for nearly all of the total
        mass of atoms, with the electrons and nuclear binding energy making minor
        contributions. Thus, the numeric value of the atomic mass when expressed
        in daltons has nearly the same value as the mass number.
        """
        return self.__data[3] * UREG.Da

    @property
    @utils.raise_on_none('atomic_radius')
    def atomic_radius(self) -> Quantity:
        """
        The atomic radius of a chemical element is a measure of the size of its atoms,
        usually the mean or typical distance from the center of the nucleus to the
        boundary of the surrounding shells of electrons. Since the boundary is not
        a well-defined physical entity, there are various non-equivalent definitions
        of atomic radius. Three widely used definitions of atomic radius are: 
        
        - Van der Waals Radius
        - Ionic Radius
        - Covalent Radius

        This property returns the covalent radius in Å (angstrom), which is one
        ten-billionth of a meter (0.000_000_000_1 m) or 1/10th of a nanometer.
        """
        return self.__data[4] * UREG.angstrom

    @property
    def number_of_neutrons(self) -> int:
        """
        Number of neutrons in a nuclide.
        """
        return self.__data[5]

    @property
    def number_of_protons(self) -> int:
        """
        Number of protons in a nuclide.
        """
        return self.__data[6]

    @property
    def number_of_electrons(self) -> int:
        """
        Number of electrons in a nuclide.
        """
        return self.__data[7]

    @property
    def period(self) -> int:
        """
        A period in the periodic table is a row of chemical elements. All elements
        in a row have the same number of electron shells. Each next element in a
        period has one more proton and is less metallic than its predecessor. Arranged
        this way, groups of elements in the same column have similar chemical and
        physical properties, reflecting the periodic law.
        """
        return self.__data[8]

    @property
    def phase(self) -> str:
        """
        Gas, liquid, and solid are known as the three states of matter or material,
        but each of solid and liquid states may exist in one or more forms. Thus,
        another term is required to describe the various forms, and the term phase
        is used. Each distinct form is called a phase; however, the concept of phase
        defined as a homogeneous portion of a system extends beyond a single material,
        because a phase may also involve several materials. For example, a homogeneous
        solution of any number of substances is a one-phase system.
        """
        return self.__data[9]

    @property
    def radioactive(self) -> bool:
        """
        Indicates whether this element is radioactive or not. Radioactivity is the
        spontaneous emission of particles or radiation (or both at the same time).
        """
        return utils.str_to_bool(self.__data[10])
    
    @property
    def natural(self) -> bool:
        """
        Tells if this element can be found naturally in nature. Note that while
        there're 118 elements on the periodic table, several elements have only
        been found in laboratories and nuclear accelerators.
        """
        return utils.str_to_bool(self.__data[11])

    @property
    def metal(self) -> bool:
        """
        A metal is a chemical element whose atoms readily lose electrons to form
        positive ions, and form metallic bonds between metal atoms and ionic bonds
        between nonmetal atoms.
        """
        return utils.str_to_bool(self.__data[12])

    @property
    def metalloid(self) -> bool:
        """
        A metalloid is a type of chemical element which has a preponderance of
        properties in between, or that are a mixture of, those of metals and nonmetals.
        There is no standard definition of a metalloid and no complete agreement
        on which elements are metalloids. Despite the lack of specificity, the term
        remains in use in the literature of chemistry.
        """
        return utils.str_to_bool(self.__data[13])

    @property
    def type(self) -> str:
        """
        Name of the group this elements belongs to, e.g. "Metal", "Noble Gas" or
        "Halogen".
        """
        return self.__data[14]

    @property
    @utils.raise_on_none('electronegativity')
    def electronegativity(self) -> float:
        """
        Electronegativity measures the tendency of an atom to attract a shared pair
        of electrons (or electron density). An atom's electronegativity is affected
        by both its atomic number and the distance at which its valence electrons
        reside from the charged nucleus. The higher the associated electronegativity,
        the more an atom or a substituent group attracts electrons.
        """
        return self.__data[15]
            
    @property
    def first_ionization(self) -> Quantity:
        """
        The ionization energy of an element is the minimum energy required to remove
        an electron from the valence shell of an isolated gaseous atom to form an ion
        The first ionization energy is the energy required to remove 1 electron from
        the valence shell.
        """
        return self.__data[16] * UREG.eV

    @property
    @utils.raise_on_none('density')
    def density(self) -> Quantity:
        """
        The density (more precisely, the volumetric mass density; also known as
        specific mass), of a substance is its mass per unit volume.
        """
        return self.__data[17] * 1000 * UREG.g / (UREG.cm ** 3)

    @property
    @utils.raise_on_none('melting_point')
    def melting_point(self) -> Quantity:
        """
        The melting point (or, rarely, liquefaction point) of a substance is the
        temperature at which it changes state from solid to liquid. At the melting
        point the solid and liquid phase exist in equilibrium. The melting point
        of a substance depends on pressure and is usually specified at a standard
        pressure such as 1 atmosphere or 100 kPa.
        """
        return self.__data[18] * UREG.K

    @property
    @utils.raise_on_none('boiling_point')
    def boiling_point(self) -> Quantity:
        """
        The boiling point of a substance is the temperature at which it can change
        its state from a liquid to a gas.
        """
        return self.__data[19] * UREG.K

    @property
    @utils.raise_on_none('number_of_isotopes')
    def number_of_isotopes(self) -> int:
        """
        Number of isotopes of this chemical element. Isotopes are atoms with the
        same number of protons but differing numbers of neutrons. In other words,
        isotopes have different atomic weights. Isotopes are different forms of a
        single element. Not all isotopes are radioactive. Stable isotopes either 
        never decay or else decay very slowly. Radioactive isotopes undergo decay.
        """
        return self.__data[20]

    @property
    @utils.raise_on_none('specific_heat')
    def specific_heat(self) -> Quantity:
        """
        The specific heat of a substance is the amount of energy required to raise
        the temperature of 1 gram of the substance by 1°C.
        """
        return self.__data[21] * UREG.J / (UREG.g * UREG.K)

    @property
    def number_of_shells(self) -> int:
        """
        Number of electron shells of this element. An Electron shell may be thought
        of as an orbit followed by electrons around an atom's nucleus.
        """
        return self.__data[22]

    @property
    @utils.raise_on_none('number_of_valance')
    def number_of_valance(self) -> int:
        """
        Number of valance electrons of this element. A valence electron is an outer
        shell electron that is associated with an atom, and that can participate
        in the formation of a chemical bond if the outer shell is not closed; in
        a single covalent bond, both atoms in the bond contribute one valence electron
        in order to form a shared pair.
        """
        return self.__data[23]

    #endregion

    #region methods

    @staticmethod
    def list(local_: bool=False) -> List[Element]:
        """
        Return a list of all elements from the periodic system of elements.
        """
        symbols = utils.query_db('elements.db', "SELECT ? FROM Element", ('Symbol',), local_=local_)
        return [Element(symbol[0]) for symbol in symbols]

    #endregion
    