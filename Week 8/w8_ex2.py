class Car(object):

    def __init__(self, colour, manufacturer, model, doors, wheels, enginesize):
        self.colour = colour
        self.manufacturer = manufacturer
        self.model = model
        self.doors = doors
        self.wheels = wheels
        self.enginesize = enginesize

    def setcolour(self, colour):
        self.colour = input("Choose the car colour: ")
        return self.colour

    def __str__(self):
        return (f"This is a {self.colour} car, made by {self.manufacturer}, it is the {self.model} model, has {self.doors} doors, {self.wheels} wheels, and a {self.enginesize} engine.")

testCar = Car(str.lower(input("What colour is the car? ")), "Volvo", "old", 3, 4, "v6")
print(testCar)
