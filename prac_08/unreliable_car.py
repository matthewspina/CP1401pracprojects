import random
from prac_08.car import Car


class UnreliableCar(Car):
    def __init__(self, name, fuel):
        super().__init__(name, fuel)
        self.reliability = 80

    def drive(self, distance):
        random_reliability = random.randint(0, 100)
        if random_reliability < self.reliability:
            distance_driven = super().drive(distance)
            print("your car has driven")
            return distance_driven
        else:
            return 0
