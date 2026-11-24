class Vehicle:
    def vehicle_type(self):
        print("This is a Vehicle")

class Car(Vehicle):
    def car_type(self):
        print("This is a Car")

class ElectricCar(Car):
    def electric_type(self):
        print("This is an Electric Car")

obj = ElectricCar()
obj.vehicle_type()
obj.car_type()
obj.electric_type()