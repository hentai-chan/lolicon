import unittest

from lolicon.physics import Planet, Satellite

class TestPlanet(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mercury = Planet('Mercury')
        cls.earth = Planet('Earth')

    @classmethod 
    def tearDown(cls):
        pass

    def test_operators(self):
        self.assertFalse(self.mercury == self.earth, msg="Mercury and Earth don't represent the same Planet")
        self.assertTrue(self.mercury != self.earth, msg="Mercury and Earth don't represent the same Planet")

    def test_repr(self):
        self.assertEqual(repr(self.earth), 'Planet(Name=Earth)', msg="Representation changed?")

    def test_mass(self):
        self.assertEqual(self.earth.mass.magnitude, 5.969999999999999e+24, msg="Expected 5.969999999999999e+24 (change of precision?)")

    def test_diameter(self):
        self.assertEqual(self.earth.diameter.magnitude, 12756, msg="Expected 12756 (change of precision?)")

    def test_gravity(self):
        self.assertEqual(self.earth.gravity.magnitude, 9.8, msg="Expected 9.8 (change of precision?)")

    def test_escape_velocity(self):
        self.assertEqual(self.earth.escape_velocity.magnitude, 11.2, msg="Expected 11.2 (change of precision?)")

    def test_rotation_period(self):
        self.assertEqual(self.earth.rotation_period.magnitude, 23.9, msg="Expected 23.9 (change of precision?)")

    def test_length_of_day(self):
        self.assertEqual(self.earth.length_of_day.magnitude, 24, msg="Expected 24 (change of precision?)")

    def test_distance_from_sun(self):
        self.assertEqual(self.earth.distance_from_sun.magnitude, 149600000.0, msg="Expected 149600000.0 (change of precision?)")

    def test_perihelion(self):
        self.assertEqual(self.earth.perihelion.magnitude, 147100000.0, msg="Expected 147100000.0 (change of precision?)")

    def test_aphelion(self):
        self.assertEqual(self.earth.aphelion.magnitude, 152100000.0, msg="Expected 152100000.0 (change of precision?)")

    def test_orbital_period(self):
        self.assertEqual(self.earth.orbital_period.magnitude, 365.2, msg="Expected 365.2 (change of precision?)")

    def test_orbital_velocity(self):
        self.assertEqual(self.earth.orbital_velocity.magnitude, 29.8, msg="Expected 29.8 (change of precision?)")

    def test_orbital_inclination(self):
        self.assertEqual(self.earth.orbital_inclination.magnitude, 0, msg="Expected 0 (change of precision?)")

    def test_orbital_eccentricity(self):
        self.assertEqual(self.earth.orbital_eccentricity, 0.017, msg="Expected 0.017 (change of precision?)")

    def test_obliquity_to_orbit(self):
        self.assertEqual(self.earth.obliquity_to_orbit.magnitude, 23.4, msg="Expected 23.4 (change of precision?)")

    def test_mean_temperature(self):
        self.assertEqual(self.earth.mean_temperature.magnitude, 15, msg="Expected 15 (change of precision?)")

    def test_surface_pressure(self):
        self.assertEqual(self.earth.surface_pressure.magnitude, 1, msg="Expected 1 (change of precision?)")

    def test_number_of_moons(self):
        self.assertEqual(self.earth.number_of_moons, 1, msg="Expected 1 (change of precision?)")

    def test_ring_system(self):
        self.assertFalse(self.earth.ring_system, msg="Expected False")

    def test_global_magnetic_field(self):
        self.assertTrue(self.earth.global_magnetic_field, msg="Expected False")

    def test_list(self):
        self.assertEqual(len(Planet.list()), 9, msg="There should be only 9 planets.")

    def test_value_error(self):
        pluto = Planet('pluto')
        with self.assertRaises(ValueError) as context:
            _ = pluto.global_magnetic_field
        self.assertTrue('Global Magnetic Field of Pluto is unknown.')

class TestSatellite(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.moon = Satellite('Moon')
        cls.triton = Satellite('Triton')

    @classmethod 
    def tearDown(cls):
        pass

    def test_operators(self):
        self.assertFalse(self.moon == self.triton, msg="Moon and Triton don't represent the same satellite.")
        self.assertTrue(self.moon != self.triton, msg="Moon and Triton don't represent the same satellite.")

    def test_repr(self):
        self.assertEqual(repr(self.moon), 'Satellite(Name=Moon)', msg="Representation changed?")

    def test_name(self):
        self.assertEqual(self.moon.name, 'Moon', msg="Expected 'Moon' (change of capitalization?)")

    def test_gm(self):
        self.assertEqual(self.moon.gm.magnitude, 4902.801, msg="Expected 4902.801 (change of precision?)")

    def test_radius(self):
        self.assertEqual(self.moon.radius.magnitude, 1737.5, msg="Expected 1737.5 (change of precision?)")

    def test_density(self):
        self.assertEqual(self.moon.density.magnitude, 3.344, msg="Expected 3.344 (change of precision?)")

    def test_magnitude(self):
        self.assertEqual(self.moon.magnitude, -12.74, msg="Expected -12.74 (change of precision?)")

    def test_magnitude(self):
        self.assertEqual(self.moon.albedo, 0.12, msg="Expected 0.12 (change of precision?)")

    def test_list(self):
        self.assertEqual(len(Satellite.list()), 177, msg="There should be only 177 satellites.")

    def test_value_error(self):
        methone, styx = Satellite('methone'), Satellite('styx')

        with self.assertRaises(ValueError) as context:
            _ = methone.magnitude
        self.assertTrue(f"Magnitude of {methone.name} is unknown.")

        with self.assertRaises(ValueError) as context:
            _ = methone.albedo
        self.assertTrue(f"Albedo of {methone.name} is unknown")

        with self.assertRaises(ValueError) as context:
            _ = styx.density
        self.assertTrue(f"Density of {styx.name} is unknown")
