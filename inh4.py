'''Problem 4 (Hybrid): Scholar Profile
Create:
- Student base class
- Sports class with a method get_sport()
- Academic inherits Student
- Scholar inherits from both Sports and Academic
- Print:
Name: John | Sport: Football | Academic Score: 90'''
class Student:
    def __init__(self,name):
        self._name=name
    def getname(self):
        return self._name
    def setname(self,name):
        self._name=name
class Sports:
    def __init__(self,sport):
        self._sport=sport
    def get_sport(self):
        return self._sport
    def setsport(self,sport):
        self._sport=sport
class Academic(Student):
    def __init__(self,name,score):
        super().__init__(name)
        self._score=score
    def getscore(self):
        return self._score
    def setscore(self,score):
        self._score=score
class Scholar(Sports,Academic):
    def __init(self,name,sport,score):
        Academic.__init__(self,name,score)
        Sports.__init__(self,sport)
    def __str__(self):
        return f"Name: {self.getname()} | Sport: {self.getsport()} | Academic score: {self.getscore()}"
s1=Scholar("John","Football",90)
print(s1)
