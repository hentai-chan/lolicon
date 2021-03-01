#!/usr/bin/env python3

import math
import unittest

from src.lolicon import mathematics
from src.lolicon import constants as const


class TestConstants(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_pi(self):
        self.assertAlmostEqual(const.PI, mathematics.pi(1_000_000), places=5)

    def test_euler(self):
        self.assertAlmostEqual(const.EULER, mathematics.euler(100), places=7)

    def test_golden_ratio(self):
        self.assertEqual(const.GOLDEN_RATIO, (1+math.sqrt(5))/2)

    def test_binary_prefixes(self):
        self.assertEqual(const.KIBI, 2**10)
        self.assertEqual(const.MEBI, 2**20)
        self.assertEqual(const.GIBI, 2**30)
        self.assertEqual(const.TEBI, 2**40)
        self.assertEqual(const.PEBI, 2**50)
        self.assertEqual(const.EXBI, 2**60)
        self.assertEqual(const.ZEBI, 2**70)
        self.assertEqual(const.YOBI, 2**80)

    def test_natural_science_constants(self):
        # reduced planck constant
        calculated = const.PLANCK / (2 * const.PI)
        self.assertAlmostEqual(const.REDUCED_PLANCK, calculated, places=9)
        # vacuum electric permittivity
        calculated = 1 / (const.MAGNETIC_PERMEABILITY * const.SPEED_OF_LIGHT**2)
        self.assertAlmostEqual(const.ELECTRIC_PERMITTIVITY, calculated, places=12)
        # characteristic impedance of vacuum
        calculated = const.MAGNETIC_PERMEABILITY * const.SPEED_OF_LIGHT
        self.assertAlmostEqual(const.CHARACTERISTIC_IMPEDANCE, calculated, places=8)
        # conductance quantum
        calculated = 2 * const.ELEMENTARY_CHARGE**2 / const.PLANCK
        self.assertAlmostEqual(const.CONDUCTANCE_QUANTUM, calculated, places=10)
        # josephson constant
        calculated = 2 * const.ELEMENTARY_CHARGE / const.PLANCK
        self.assertAlmostEqual(const.JOSEPHSON.magnitude, calculated.magnitude, delta=16_983.625)
        # von klitzing constant
        calculated = const.PLANCK / const.ELEMENTARY_CHARGE**2
        self.assertAlmostEqual(const.VON_KLITZING, calculated, places=4)
        # magnetic flux quantum
        calculated = const.PLANCK / (2 * const.ELEMENTARY_CHARGE)
        self.assertAlmostEqual(const.MAGNETIC_FLUX_QUANTUM, calculated, places=9)
        # inverse conductance quantum
        calculated = const.PLANCK / (2 * const.ELEMENTARY_CHARGE**2)
        self.assertAlmostEqual(const.INVERSE_CONDUCTANCE_QUANTUM, calculated, places=4)
        # bohr magneton
        calculated = const.ELEMENTARY_CHARGE * const.REDUCED_PLANCK / (2 * const.ELECTRON_MASS)
        self.assertAlmostEqual(const.BOHR_MAGNETON, calculated, places=12)
        # nuclear magneton
        calculated = const.ELEMENTARY_CHARGE * const.REDUCED_PLANCK / (2 * const.PROTON_MASS)
        self.assertAlmostEqual(const.NUCLEAR_MAGNETON, calculated, places=12)
        # fine structure constant
        calculated = const.ELEMENTARY_CHARGE**2 / (4 * const.PI * const.ELECTRIC_PERMITTIVITY * const.REDUCED_PLANCK * const.SPEED_OF_LIGHT)
        self.assertAlmostEqual(const.FINE_STRUCTURE, calculated, places=10)
        # inverse fine structure constant
        calculated = 1 / const.FINE_STRUCTURE
        self.assertAlmostEqual(const.INVERSE_FINE_STRUCTURE, calculated, places=8)
        # bohr radius
        calculated = const.REDUCED_PLANCK * const.INVERSE_FINE_STRUCTURE / (const.ELECTRON_MASS * const.SPEED_OF_LIGHT)
        self.assertAlmostEqual(const.BOHR_RADIUS, calculated, places=12)
        # classic electron radius
        calculated = const.ELEMENTARY_CHARGE**2 / (4 * const.PI * const.ELECTRIC_PERMITTIVITY * const.ELECTRON_MASS * const.SPEED_OF_LIGHT**2)
        self.assertAlmostEqual(const.ELECTRON_RADIUS, calculated, places=12)
        # hartree energy
        calculated = 2 * const.RYDBERG * const.PLANCK * const.SPEED_OF_LIGHT
        self.assertAlmostEqual(const.HARTREE_ENERGY, calculated, places=12)
        # quantum of circulation
        calculated = const.PLANCK / (2 * const.ELECTRON_MASS)
        self.assertAlmostEqual(const.QUANTUM_OF_CIRCULATION, calculated, places=12)
        # rydberg constant
        calculated = const.FINE_STRUCTURE**2 * const.ELECTRON_MASS * const.SPEED_OF_LIGHT / (2 * const.PLANCK)
        self.assertAlmostEqual(const.RYDBERG, calculated, places=4)
        # thomson cross section
        calculated = 8/3 * const.PI * const.ELECTRON_RADIUS**2
        self.assertAlmostEqual(const.THOMSON_CROSS_SECTION, calculated, places=12)
        # weak mixing angle
        calculated = 1 - const.W2Z_MASS_RATIO**2
        self.assertAlmostEqual(const.WEAK_MIXING_ANGLE, calculated, places=5)
        # faraday constant
        calculated = const.AVOGADRO * const.ELEMENTARY_CHARGE
        self.assertAlmostEqual(const.FARADAY, calculated, places=5)
        # universal gas constant
        calculated = const.AVOGADRO * const.BOLTZMANN
        self.assertAlmostEqual(const.UNIVERSAL_GAS_CONSTANT, calculated, places=9)
        # molar mass constant
        calculated = const.MOLAR_MASS_CARBON12 / 12
        self.assertAlmostEqual(const.MOLAR_MASS_CONSTANT, calculated, places=12)
        # stefan-boltzmann constant
        calculated = const.PI**2 * const.BOLTZMANN**4 / (60 * const.REDUCED_PLANCK**3 * const.SPEED_OF_LIGHT**2)
        self.assertAlmostEqual(const.STEFAN_BOLTZMANN, calculated, places=9)
        # first radiation constant
        calculated = 2 * const.PI * const.PLANCK * const.SPEED_OF_LIGHT**2
        self.assertAlmostEqual(const.FIRST_RADIATION, calculated, places=9)
        # first radiation constant for spectral radiance
        calculated = const.FIRST_RADIATION / const.PI
        self.assertAlmostEqual(const.FIRST_RADIATION_SPECTRAL_RADIANCE, calculated, places=9)
        # second radiation constant
        calculated = const.PLANCK * const.SPEED_OF_LIGHT / const.BOLTZMANN
        self.assertAlmostEqual(const.SECOND_RADIATION_CONSTANT, calculated, places=9)
