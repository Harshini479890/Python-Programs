'''1. Store and Retrieve Student Records
Scenario:
A college wants to store student details (roll number, name, marks) in a binary file for
security. Write a program to:
 Accept details for n students and store them in a binary file using pickle.
 Read the file and display all student records.
Key Focus: Writing and reading structured data using binary mode (wb, rb).'''
import pickle
def writer(filename):
    n=int(input("Enter number of students: "))
    stud=[]
    for i in range(n):
        roll=int(input(f"Enter roll no of s{i+1}: "))
        name=input(f"Enter name of s{i+1}: ")
        marks=float(input(f"Enter marks of s{i+1}: "))
        stud.append((roll,name,marks))

        with open(filename,"wb") as f:
            pickle.dump(stud,f)
        print("Written\n")
def readr(filename):
    with open(filename,"rb") as f:
        stud=pickle.load(f)
    print("Student records:")
    for s in stud:
        print (f"Roll: {s[0]} | Name: {s[1]}  | Marks: {s[2]}")
filename="students.dat"
writer(filename)
readr(filename)
