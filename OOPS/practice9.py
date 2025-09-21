#                            Inheritance 

# Inheritance is a way to form new classes using classes that have already been defined.
# ( single level inheritance)


class Car:
    @staticmethod
    def start():
        print("Car started")

    @staticmethod
    def stop():
        print("Car stopped")

class Tatacar(Car):
    def __init__(self, name):
        self.name = name

car1 = Tatacar("Tata")
car2 = Tatacar("toyata")

print(car1.name)
print(car1.start())


# multiple  level  inheritance


class Car:
    @staticmethod
    def start():
        print("Car started")

    @staticmethod
    def stop():
        print("Car stopped")

class Tatacar(Car):
    def __init__(self, brand):
        self.brand = brand

class fortuner(Tatacar):
    def __init__(self, type):
        self.type = type

car1 = fortuner("SUV")
car2 = fortuner("Hatchback")
car1.start()


# multiple inheritance

class A:
    varA = "class A"

class B:
    varB = "class B"

class C(A, B):
    varC = "class C"

c1 = C()

print(c1.varA)
print(c1.varB)
print(c1.varC)