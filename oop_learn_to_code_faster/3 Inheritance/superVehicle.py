# Parent class
class Vehicle:
    def vehicle_data(self):
        print('This is Vehicle class')


# Child class
class Car(Vehicle):
    def car_data(self):
        print('This is Car class')


# Child class
class Bike(Vehicle):
    def bike_data(self):
        print('This is Bike class')


# Objects based on Car
car_matiz = Car()
bike_motozicl = Bike()

# Get Vehicle data
car_matiz.vehicle_data()
car_matiz.car_data()
print('----------------')
bike_motozicl.vehicle_data()
bike_motozicl.car_data()
