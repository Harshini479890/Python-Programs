'''Problem 2: Student Grade Calculator
You are developing a grading system for an educational institution.
Create a Student class that:
- Has private attributes:
- __name (string)
- __marks (integer)
- Use setter for marks to ensure:
- Marks must be in the range 0–100, else raise a ValueError.
- Add a method get_grade() that returns:
- A for marks ≥ 90
- B for marks ≥ 75
- C for marks ≥ 50
- F for marks < 50
- Display details using __str__ in this format:
Student: John | Marks: 85 | Grade: B'''
class Student:
    def __init__(self,name,marks):
        self.__name=name
        self.__marks=marks
    def setmark(self,marks):
        if marks>0 and marks<100:
            self.__marks=marks
        else:
            raise ValueError("Marks must be between 0 and 100.")
    def getgrade(self):
        if self.__marks>=90:
            return 'A'
        elif self.__marks>=75:
            return 'B'
        elif self.__marks>=50:
            return 'C'
        else:
            return 'F'
    def __str__(self):
        return f"Student: {self.__name} | Marks: {self.__marks} | Grade: {self.getgrade()}"
if __name__=="__main__":
    while True:
        print("1.Details\n2.Display\n3.Exit\n")
        ch=int(input("Enter your choice "))
        if ch==1:
            name=input("Enter the name: ")
            marks=int(input("Enter the marks: "))
            try:
                s1=Student(name,marks)
                print("Student details saved.")
            except ValueError as e:
                print("Error: ",e)
        elif ch==2:
            print(s1)
        elif ch==3:
            print("Exiting..")
            break
        else:
            print("Invalid choice.")
