'''Problem 2: Car Engine
Create:
- Engine class: horsepower.
- Car class contains an Engine object.
- Print:
Car Model: Tesla | Engine Power: 500 HP'''
class Engine:
    def __init__(self,ep):
        self.ep=ep
class Car:
    def __init__(self,cm,eng):
        self.cm=cm
        self.eng=eng
    def __str__(self):
        return f"Car Model: {self.cm} | Engine Power: {self.eng.ep}"
e1=Engine("500 HP")
c1=Car("Tesla",e1)
print(c1)
