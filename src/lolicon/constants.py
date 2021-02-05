#!/usr/bin/env python3

from __future__ import annotations

from pint.quantity import Quantity

from .utils import UREG

#region computer science

# decimal prefixes
Yocto = 1e-24
Zepto = 1e-21
Atto = 1e-18
Femto = 1e-15
Pico = 1e-12
Nano = 1e-9
Micro = 1e-6
Milli = 1e-3
Centi = 1e-2
Deci = 1e-1
Deka = 1e+1
Hecto = 1e+2
Kilo = 1e+3
Mega = 1e+6
Giga = 1e+9
Tera = 1e+12
Peta = 1e+15
Exa = 1e+18
Zetta = 1e+21
Yotta = 1e+24

# binary prefixes
Kibi = 1024
Mebi = 1_048_576
Gibi = 1_073_741_824
Tebi = 1_099_511_627_776
Pebi = 1_125_899_906_842_624
Exbi = 1_152_921_504_606_846_976
Zebi = 1_180_591_620_717_411_303_424
Yobi = 1_208_925_819_614_629_174_706_176

#endregion computer science

#region physics

MassOfProton: Quantity = 1.672_621_923_69e-27 * UREG.kg
ElectricChargeOfProton: Quantity = 1.602_176_634e-19 * UREG.C

MassOfElectron: Quantity = 	9.109_383_701_5e-31 * UREG.kg
ElectricChargeOfElectron: Quantity = -ElectricChargeOfProton.magnitude * UREG.C

MassOfNeutron: Quantity = 1.674_927_498_04e-27 * UREG.kg
ElectricChargeOfNeutron: Quantity = 0 * UREG.C

SpeedOfLight: Quantity = 299_792_458 * UREG.m / UREG.s
GravitationalConstant: Quantity = 6.674_30e-11 * (UREG.m ** 3) / (UREG.kg * (UREG.s ** 2))

#endregion physics

#region chemistry

AvogadroNumber: Quantity = 6.022_140_76e+23 * (1 / UREG.mol)
BoltzmannConstant: Quantity = 1.380_649e-23 * UREG.J / UREG.K
UniversalGasConstant: Quantity = 8.314_462_618_153_24 * UREG.J / (UREG.K * UREG.mol)

#endregion chemistry