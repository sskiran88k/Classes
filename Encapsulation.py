class Circle:
    def __init__(self, radius):
        self.__radius = radius # __ indicates a private attribute

    def get_radius(self):
        return self.__radius
    
obj=Circle(2.5)
print(obj.get_radius())
