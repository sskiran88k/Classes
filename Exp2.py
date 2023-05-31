class Car:
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color
        self.engine_status = False

    def start_engine(self):
        if self.engine_status:
            print(f"The {self.make} {self.model}'s engine is already running.")
        else:
            self.engine_status = True
            print(f"The {self.make} {self.model}'s engine is now running.")
    
    def stop_engine(self):
        if not self.engine_status:
            print(f"The {self.make} {self.model}'s engine is already stopped.")
        else:
            self.engine_status = False
            print(f"The {self.make} {self.model}'s engine has stopped.")
my_car = Car("Toyota", "Corolla", "Red")
my_car.start_engine()
my_car.stop_engine()
