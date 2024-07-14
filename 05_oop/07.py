# 7. Static Method
# Problem: Add a static method to the Car class that returns a general description of a car.

class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
    
    def display_info(self):
        return f"{self.__brand} {self.model}"

    @staticmethod
    def general_description():
        return "Cars are means of Transport"

my_car = Car("toyota", "Innova")
print(my_car.general_description())
# print(Car.general_description())

