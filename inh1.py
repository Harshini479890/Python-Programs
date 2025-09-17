'''Problem 1 (Single): Employee Information System
Create a base class Person and a derived class Employee:
- Person → Attributes: name, age.
- Employee → Adds: salary, designation.
- Use getters/setters for each attribute.
- Print details using __str__:
Name: John | Age: 30 | Salary: ₹50000 | Designation: Manager'''
class Person:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    def getage(self):
        return self.__age
    def getname(self):
        return self.__name
    def setage(self,age):
        if age>0:
            self.__age=age
        else:
            print("Invalid age")
    def setname(self,name):
        self.__name=name
    def __str__(self):
        return f"Name: {self.__name} | Age: {self.__age}"
class Employee(Person):
    def __init__(self,name,age,salary,designation):
        super().__init__(name,age)
        self.__salary=salary
        self.__designation=designation
    def getsal(self):
        return self.__salary
    def getdesig(self):
        return self.__designation
    def setsal(self,sal):
        if sal>=0:
            self.__salary=sal
        else:
            print("Salary cannot be negative.")
    def setdesig(self,desig):
        self.__designation=desig
    def __str__(self):
        return (f"Name: {self.getname()} | Age: {self.getage()} | Salary: {self.__salary} | Designation: {self.__designation}")
e1=Employee("John",30,50000,"Manager")
print(e1)
