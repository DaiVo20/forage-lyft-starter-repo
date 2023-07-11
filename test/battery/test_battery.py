import unittest
from datetime import datetime
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery


class TestNubbinBattery(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        engine = NubbinBattery(today, last_service_date)
        self.assertTrue(engine.needs_service())
    
    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        engine = NubbinBattery(today, last_service_date)
        self.assertFalse(engine.needs_service())

class TestSpindlerBattery(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        engine = SpindlerBattery(today, last_service_date)
        self.assertTrue(engine.needs_service())
    
    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        engine = SpindlerBattery(today, last_service_date)
        self.assertFalse(engine.needs_service())


if __name__ == '__main__':
    unittest.main()
