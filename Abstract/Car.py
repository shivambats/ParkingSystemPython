from datetime import datetime


class Car:
    def __init__(self, registration_number, spot: str):
        self.registration_number = registration_number
        self.parked_at = datetime.now()
        self.spot = spot

    def getFare(self):
        time_spent = max((datetime.now() - self.parked_at).seconds / 3600, 1)
        return self.standard_fare * time_spent
