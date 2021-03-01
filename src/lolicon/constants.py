#!/usr/bin/env python3

"""
Constants
=========

In STEM it is often necessary to embed constants in equations or expressions. This
namespace provides access to constants used in

- Mathematics
- Computer Science
- Natural Sciences

These values should be accurate enough for students enrolled in high school or
undergraduate students to solve homework problems.

Example
-------
```
>>> from lolicon import constants as const
>>> print(const.PROTON_MASS)
<Quantity(1.67262192e-27, 'kilogram')>
```

References
----------
- <https://pint.readthedocs.io/en/stable/>
- <https://en.wikipedia.org/wiki/List_of_physical_constants>
"""

from __future__ import annotations

from pint.quantity import Quantity

from .utils import UREG

#region mathematics

PI: float = 3.141_592_653_589_793
EULER: float = 2.718_281_828_459_045
GOLDEN_RATIO: float = 1.618_033_988_749_895

#endregion

#region computer science

GOOGOL = 1e+100

# decimal prefixes
YOCTO = 1e-24
ZEPTO = 1e-21
ATTO = 1e-18
FEMTO = 1e-15
PICO = 1e-12
NANO = 1e-9
MICRO = 1e-6
MILLI = 1e-3
CENTI = 1e-2
DECI = 1e-1
DEKA = 1e+1
HECTO = 1e+2
KILO = 1e+3
MEGA = 1e+6
GIGA = 1e+9
TERA = 1e+12
PETA = 1e+15
EXA = 1e+18
ZETTA = 1e+21
YOTTA = 1e+24

# binary prefixes
KIBI = 1024
MEBI = 1_048_576
GIBI = 1_073_741_824
TEBI = 1_099_511_627_776
PEBI = 1_125_899_906_842_624
EXBI = 1_152_921_504_606_846_976
ZEBI = 1_180_591_620_717_411_303_424
YOBI = 1_208_925_819_614_629_174_706_176

#endregion computer science

#region natural sciences

SPEED_OF_LIGHT: Quantity = 299_792_458 * UREG.m / UREG.s
PLANCK: Quantity = 6.626_070_15e-34 * UREG.J * UREG.s
REDUCED_PLANCK: Quantity = 1.054_571_817e-34 * UREG.J * UREG.s
NEWTONIAN_GRAVITATION: Quantity = 6.674_301_5e-11 * (UREG.m ** 3) / (UREG.kg * (UREG.s ** 2))
ELECTRIC_PERMITTIVITY: Quantity = 8.854_187_812_813e-12 * UREG.F / UREG.m
MAGNETIC_PERMEABILITY: Quantity = 1.256_637_062_121_9e-6 * UREG.N / UREG.A**2
CHARACTERISTIC_IMPEDANCE: Quantity = 376.730_313_668 * UREG.ohm
ELEMENTARY_CHARGE: Quantity = 1.602_176_634e-19 * UREG.C
HYPERFINE_TRANSITION_FREQUENCY: Quantity = 9_192_631_770 * UREG.Hz
AVOGADRO: Quantity = 6.022_140_76e+23 * (1 / UREG.mol)
BOLTZMANN: Quantity = 1.380_649e-23 * UREG.J / UREG.K
CONDUCTANCE_QUANTUM: Quantity = 7.748_091_729e-5 * UREG.S
JOSEPHSON: Quantity = 483_597.8484e+9 * UREG.Hz / UREG.V # 483 597.8484
COULOMB: Quantity = 8.987_551_792_314e+9 * UREG.kg * UREG.m**3 / (UREG.s**2 * UREG.C**2)
VON_KLITZING: Quantity = 25_812.807_45 * UREG.ohm
MAGNETIC_FLUX_QUANTUM: Quantity = 2.067_833_848e-15 * UREG.Wb
INVERSE_CONDUCTANCE_QUANTUM: Quantity = 12_906.403_72 * UREG.ohm
BOHR_MAGNETON: Quantity = 9.274_010_078_328e-24 * UREG.J / UREG.T
NUCLEAR_MAGNETON: Quantity = 5.050_783_746_115e-27 * UREG.J / UREG.T
FINE_STRUCTURE: float = 7.297_352_569_311e-3
INVERSE_FINE_STRUCTURE: float = 137.035_999_084_21
ELECTRON_MASS: Quantity = 9.109_383_701_528e-31 * UREG.kg
PROTON_MASS: Quantity = 1.672_621_923_695_1e-27 * UREG.kg
NEUTRON_MASS: Quantity = 1.674_927_498_0495e-27 * UREG.kg
BOHR_RADIUS: Quantity = 5.291_772_109_038_0e-11 * UREG.m
ELECTRON_RADIUS: Quantity = 2.817_940_326_213e-15 * UREG.m
ELECTRON_G_FACTOR: float = -2.002_319_304_362_563_5
FERMI_COUPLING: Quantity = 1.166_378_76e-5 * UREG.Ge / UREG.V**2
HARTREE_ENERGY: Quantity = 4.359_744_722_207_185e-18 * UREG.J
QUANTUM_OF_CIRCULATION: Quantity = 3.636_947_551_611e-4 * UREG.m**2 / UREG.s
RYDBERG: Quantity = 10_973_731.568_160_21 / UREG.m
THOMSON_CROSS_SECTION: Quantity = 6.652_458_732_160e-29 * UREG.m**2
W2Z_MASS_RATIO: float = 0.881_531_7
WEAK_MIXING_ANGLE: float = 0.222_903
ATOMIC_MASS: Quantity = 1.660_539_066_605e-27 * UREG.kg
FARADAY: Quantity = 96_485.332_12 * UREG.C / UREG.mol
UNIVERSAL_GAS_CONSTANT: Quantity = 8.314_462_618 * UREG.J / (UREG.K * UREG.mol)
MOLAR_MASS_CONSTANT: Quantity = 0.999_999_999_653e-3 * UREG.kg / UREG.mol
STEFAN_BOLTZMANN: Quantity = 5.670_374_419e-8 * UREG.W / (UREG.m**2 * UREG.K**4)
FIRST_RADIATION: Quantity = 3.741_771_852e-16 * UREG.W * UREG.m**2
FIRST_RADIATION_SPECTRAL_RADIANCE: Quantity = 1.191_042_972e-16 * UREG.W * UREG.m**2 / UREG.sr
MOLAR_MASS_CARBON12: Quantity = 11.999_999_995_836e-3 * UREG.kg / UREG.mol
MOLAR_PLANCK_CONSTANT: Quantity = 3.990_312_712e-10 * UREG.J / (UREG.Hz * UREG.mol)
SECOND_RADIATION_CONSTANT: Quantity = 1.438_776_877e-2 * UREG.m * UREG.K
WIEN_WAVELENGTH_DISPLACEMENT_LAW: Quantity = 2.897_771_955e-3 * UREG.m * UREG.K
WIEN_FREQUENCY_DISPLACEMENT_LAW: Quantity = 5.878_925_757e+10 * UREG.Hz / UREG.K
WIEN_ENTROPY_DISPLACEMENT_LAW: Quantity = 3.002_916_077e-3 * UREG.m * UREG.K

#endregion natural sciences
