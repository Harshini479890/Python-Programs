'''Problem 2 (Multiple): Amphibious Bird Abilities
Create a class hierarchy:
- Flyer class → Method βly() returns 'Can Fly'.
- Swimmer class → Method swim() returns 'Can Swim'.
- AmphibiousBird inherits from both and overrides __str__ to show:
This bird can fly and swim.'''
class Flyer:
    def fly(self):
        return "Can Fly"
class Swimmer:
    def swim(self):
        return "Can Swim"
class Amp(Flyer,Swimmer):
    def __str__(self):
        return "This bird can fly and swim."
a1=Amp()
print(a1.fly())
print(a1.swim())
print(a1)
