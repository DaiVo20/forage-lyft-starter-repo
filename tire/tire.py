from abc import ABC


class Tire(ABC):
    def __init__(self, tire_wear_sensors):
        self.tire_wear_sensors = tire_wear_sensors

    def needs_service(self):
        pass