# 5. Polymorphism
# Problem: Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviors.

class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    
    def full_name(self):
        return f"{self.brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
class ElectriCar(Car):
    def __init__(self, brand, model, battery_size):
       super().__init__(brand, model)
       self.battery_size = battery_size
    
    def fuel_type(self):
        return "Electric Charge"

    

my_tesla= ElectriCar("Tesla", "model S", "85kWH")
print(my_tesla.fuel_type())

Safari = Car("Tata","Safari")
print(Safari.fuel_type())