# 8. Property Decorators
# Problem: Use a property decorator in the Car class to make the model attribute read-only.

class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
    
    def display_info(self):
        return f"{self.__brand} {self.__model}"

    @property
    def model(self):
        return self.__model

my_car = Car("toyota", "Innova")
# my_car.model = "corolla"
print(my_car.model)