class Car:
    #constructor Called
     def __init__(self, brand, model, color):
         self.brand = brand
         self.model = model
         self.color = color
     def car_details(self):
         return f"Brand :{self.brand}, Model :{self.model}, color:{self.color}"
     def start(self):
         return f"{self.brand} {self.model} is starting."
my_car=Car("toyota","corola","red")
print(my_car.car_details())
print(my_car.start())

#inheritance
class Electriccar(Car):
    def __init__(self,brand,model,color,battery_capacity):
        super().__init__(brand,model,color)
        self.battery_capacity = battery_capacity
    def car_details(self):
        original_details = super().car_details()
        return f"{original_details},Battery Capacity: {self.battery_capacity} kwh"
    def charge(self):
        return f"{self.brand} {self.model} is charging."
my_electric_car = Electriccar("Tesla","Model s","white",100)
print(my_electric_car.car_details())
print(my_electric_car.start())
print(my_electric_car.charge())


#Polymorphism
class Electriccar(Car):
    def __init__(self,brand,model,color,battery_capacity):
        super().__init__(brand,model,color)
        self.battery_capacity = battery_capacity

    def car_details(self):
        original_details = super().car_details()
        return f"{original_details},Battery capacity :{self.battery_capacity} kwh"

    def start(self):
        return f"{self.brand} {self.model} is starting silently."


regular_car = Car("honda", "civic", "blue")
electric_car = Electriccar("Tesla","Model 9", "black", 34)

print(regular_car.start())
print(electric_car.start())

