# 4. Encapsulation
# Problem: Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it.

class Car:
    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model
    
    def get_brand(self):
        return self.__brand
    
    def full_name(self):
        return f"{self.brand} {self.model}"


my_car = Car("Toyota","corolla")   
print(my_car.get_brand())