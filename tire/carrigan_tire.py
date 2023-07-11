from tire.tire import Tire

class CarriganTire(Tire):
    def needs_service(self):
        for ele in self.tire_wear_sensors:
            if ele >= 0.9:
                return True
        return False