class Car:
    def __init__(self,brand,model,color):
        self.model = brand
        self._brand = model
        self._color = color


    def car_details(self):
        return f"Brrand :{self._brand}, and Model is {self.model},and color is {self._color}"


my_car = Car("bmw","mi78","Black")
print(my_car.model)
print(my_car.car_details())