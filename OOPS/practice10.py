#  super method = super() method is used to access methods of the parent class

class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("Car started")

    @staticmethod
    def stop():
        print("Car stopped")

class Toyota(Car):
    def __init__(self, name, type):
        self.name = name   
        super().__init__(type)   # super() method is used to access methods of the parent class

car1 = Toyota("Toyota", "SUV")
print(car1.type)