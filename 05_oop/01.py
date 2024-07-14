# 1. Basic Class and Object
# Problem: Create a Car class with attributes like brand and model. Then create an instance of this class


class Car:
    def __init__(self, brand, Model):
        self.brand = brand
        self.Model = Model

my_car = Car("Toyata","Corolla")
print(my_car.brand)
print(my_car.Model)