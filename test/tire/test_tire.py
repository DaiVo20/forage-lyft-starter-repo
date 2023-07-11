import unittest
from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire

class TestCarriganTire(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        tire_wear_sensors = [0.95, 0.1, 0.2, 0.3]
        tire = CarriganTire(tire_wear_sensors)
        self.assertTrue(tire.needs_service())

    def test_tire_should_not_be_serviced(self):
        tire_wear_sensors = [0.1, 0.1, 0.2, 0.3]
        tire = CarriganTire(tire_wear_sensors)
        self.assertFalse(tire.needs_service())

class TestOctoprimeTire(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        tire_wear_sensors = [0.9, 0.9, 0.9, 0.9]
        tire = CarriganTire(tire_wear_sensors)
        self.assertTrue(tire.needs_service())

    def test_tire_should_not_be_serviced(self):
        tire_wear_sensors = [0.2, 0.1, 0.2, 0.3]
        tire = CarriganTire(tire_wear_sensors)
        self.assertFalse(tire.needs_service())

if __name__ == "___main___":
    unittest.main()