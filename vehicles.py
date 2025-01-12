# Base class
class Vehicle:
    def move(self):
        pass

# Subclass Car
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

# Subclass Plane
class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# Creating instances
car = Car()
plane = Plane()

mode_of_transport = input("What mode of transport are you using: ").lower()
if mode_of_transport == "car":
    car.move()
elif mode_of_transport == "plane":
    plane.move()
else:
    print("Unknown mode of transport")
