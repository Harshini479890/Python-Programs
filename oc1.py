'''Problem 1: Employee Address System
Create:
- Address class: city, state.
- Employee class has an Address object.
- Print:
Employee: John | City: Chennai | State: Tamil Nadu'''
class Address:
    def __init__(self,city,state):
        self.city=city
        self.state=state
class Employee:
    def __init__(self,name,add):
        self.name=name
        self.add=add
    def __str__(self):
        return f"Employee: {self.name} | City: {self.add.city} | State: {self.add.state}"
a1=Address("Chennai","tamilnadu")
e1=Employee("John",a1)
print(e1)
