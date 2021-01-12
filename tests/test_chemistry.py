import unittest

from lolicon.chemistry import Element

class TestElement(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.gold = Element('Au')
        cls.hydrogen = Element('H')

    @classmethod 
    def tearDown(cls):
        pass

    def test_operators(self):
        self.assertFalse(self.hydrogen == self.gold, msg="Hydrogen and gold don't represent the same Element")
        self.assertTrue(self.hydrogen != self.gold, msg="Hydrogen and gold don't represent the same Element")

    def test_repr(self):
        self.assertEqual(repr(self.gold), 'Element(AtomicNumber=79)', msg="Representing formatting changed")

    def test_name(self):
        self.assertEqual(self.gold.name, 'Gold')

    def test_atomic_number(self):
        self.assertEqual(self.gold.atomic_number, 79)

    def test_atomic_mass(self):
        self.assertEqual(self.gold.atomic_mass.magnitude, 196.967)

    def test_atomic_radius(self):
        self.assertEqual(self.gold.atomic_radius.magnitude, 1.8)

    def test_number_of_neutrons(self):
        self.assertEqual(self.gold.number_of_neutrons, 118)

    def test_number_of_protons(self):
        self.assertEqual(self.gold.number_of_protons, 79)

    def test_number_of_electrons(self):
        self.assertEqual(self.gold.number_of_electrons, 79)

    def test_period(self):
        self.assertEqual(self.gold.period, 6)

    def test_phase(self):
        self.assertEqual(self.gold.phase, 'solid')

    def test_radioactive(self):
        self.assertFalse(self.gold.radioactive)

    def test_natural(self):
        self.assertTrue(self.gold.natural)

    def test_metal(self):
        self.assertTrue(self.gold.metal)

    def test_metalloid(self):
        self.assertFalse(self.gold.metalloid)

    def test_type(self):
        self.assertEqual(self.gold.type, 'Transition Metal')

    def test_electronegativity(self):
        self.assertEqual(self.gold.electronegativity, 2.54)

    def test_first_ionization(self):
        self.assertEqual(self.gold.first_ionization.magnitude, 9.2255)

    def test_density(self):
        self.assertEqual(self.gold.density.magnitude, 19300.0)

    def test_melting_point(self):
        self.assertEqual(self.gold.melting_point.magnitude, 1337.73)

    def test_boiling_point(self):
        self.assertEqual(self.gold.boiling_point.magnitude, 3129.0)

    def test_number_of_isotopes(self):
        self.assertEqual(self.gold.number_of_isotopes, 21)

    def test_specific_heat(self):
        self.assertEqual(self.gold.specific_heat.magnitude, 0.129)

    def test_number_of_shells(self):
        self.assertEqual(self.gold.number_of_shells, 6)

    def test_number_of_valance(self):
        with self.assertRaises(ValueError) as context:
            number_of_valance = self.gold.number_of_valance
        self.assertTrue(f'Number of valance of {self.gold.name} is None', str(context.exception))

    def test_list(self):
        self.assertEqual(len(Element.list()), 118, msg="There should be only 118 elements.")
     