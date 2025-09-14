'''3. Employee Salary Calculator
Description:
An organization wants to calculate employees’ net salary. Each employee has a name,
employee ID, and basic salary. The company name is the same for all employees.
What to do:
 Create a class named Employee.
 Define instance variables for name, emp_id, and basic_salary.
 Define a class variable for company_name.
 Create a constructor to initialize the employee details.
 Write two methods:
o calculate_salary() → Calculate net salary as basic_salary + 5000 (allowance).
o display_employee() → Show employee details along with net salary.
 Create two employee objects, calculate and display their salary details.'''
class Employee:
    def __init__(self,name,empid,bs):
        self.name=name
        self.empid=empid
        self.bs=bs
    companyn="Amazon"
    def cal(self):
        self.ns=self.bs+5000
    def display(self):
        print(f"Name : {self.name}")
        print(f"ID : {self.empid}")
        print(f"Net salary : {self.ns}")
        print(f"Company name : {Employee.companyn}")
e1=Employee("Harshini",12,50000)
e2=Employee("Navyasri",11,60000)
e1.cal()
e2.cal()
print("Employee details ")
e1.display()
e2.display()
