'''Problem 3 (Multilevel): Laptop Specifications
Create classes:
- Device → Attribute: brand.
- Computer (inherits Device) → Adds processor.
- Laptop (inherits Computer) → Adds battery_life.
- All attributes should be protected and accessed using getters/setters.
- Display details using __str__:
Brand: Dell | Processor: i7 | Battery Life: 10 hours'''
class Device:
    def __init__(self,brand):
        self._brand=brand
    def getbrand(self):
        return self._brand
    def setbrand(self,brand):
        self._brand=brand
class Computer(Device):
    def __init__(self,brand,processor):
        super().__init__(brand)
        self._processor=processor
    def getproc(self):
        return self._processor
    def setproc(self,processor):
        self._processor=processor
class Laptop(Computer):
    def __init__(self,brand,processor,batlife):
        super().__init__(brand,processor)
        self._batlife=batlife
    def getbat(self):
        return self._batlife
    def setbat(self,batlife):
        self._batlife=batlife
    def __str__(self):
        return f"Brand: {self.getbrand()} | Processor: {self.getproc()} | Battery Life: {self._batlife}"
l1=Laptop("Dell","i7","10 hours")
print(l1)
        
