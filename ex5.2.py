'''Q2. Division Scenario – A teacher wants to calculate the average marks of students. Write a
program that:
 Takes total marks and number of students as input.
 Calculates the average.
 If the user enters 0 for the number of students, handle the exception and display:
"Error: Cannot divide by zero. Please check the number of students."
Hint to students: Use try-except and handle ZeroDivisionError.'''
def avg():
    n=int(input("Enter the number of students "))
    tot=int(input("Enter total marks "))
    try:
        avg=tot/n
        print(avg)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero. Please check the number of students.")
    else:
        print("Success")
avg()
