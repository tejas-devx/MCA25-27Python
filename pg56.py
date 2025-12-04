# Create class Engine(_power) and Wheels(_size).Derive the class Car(_model) from Engine & Wheels.Display details of the car using method overriding.

class Engine:
    def __init__(self, power):
        self.power = power

    def display(self):
        print("Engine Power:", self.power)


class Wheels:
    def __init__(self, size):
        self.size = size

    def display(self):
        print("Wheel Size:", self.size)


class Car(Engine, Wheels):
    def __init__(self, model, power, size):
        Engine.__init__(self, power)
        Wheels.__init__(self, size)
        self.model = model

    def display(self):          # method overriding
        print("Car Model:", self.model)
        Engine.display(self)
        Wheels.display(self)


model = input("Enter car model: ")
power = input("Enter engine power: ")
size = input("Enter wheel size: ")

c = Car(model, power, size)
c.display()
