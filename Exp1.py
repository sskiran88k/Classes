class Car:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand

    def display(self):
        print(f"This car is a {self.color} {self.brand}")
my_car = Car('red', 'Toyota')
print(my_car.color)  # prints: red
print(my_car.brand)  # prints: Toyota
my_car.display()  # prints: This car is a red Toyota
