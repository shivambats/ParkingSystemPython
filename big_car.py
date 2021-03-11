from Abstract.Car import Car

STANDARD_FARE = 20


class BigCar(Car):
    def __init__(self, *args, **kwargs):
        Car.__init__(self, *args, **kwargs)
        self.standard_fare = STANDARD_FARE
