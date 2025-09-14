'''1. Student Information System
Description:
You are asked to design a simple system to store student details using a class. Each student
has a name, roll number, and department. All students belong to the same college.
What to do:
 Create a class named Student.
 Define instance variables for name, roll_no, and department.
 Define a class variable for the college name (common for all students).
 Create a constructor (__init__) to initialize the instance variables.
 Write a method display_info() to print the student details including the college name.
 Create at least 3 objects and display their details using the method.'''
class Student:
    clgname="SASTRA"
    def __init__(self,name,rollno,dept):
        self.name=name
        self.rollno=rollno
        self.dept=dept
    def display_info(self):
        print(f"Roll number : {self.rollno},Name : {self.name},Department : {self.dept},College name : {Student.clgname}")
s1=Student("Rani",1,"CSE")
s2=Student("Raju",2,"ECE")
s3=Student("Radha",3,"CSE")
print("Student details ")
s1.display_info()
s2.display_info()
s3.display_info()
