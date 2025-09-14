'''1. Student Diary System
A school wants to maintain a diary for each student where daily activities are stored in a
text file named after the student (e.g., Ravi.txt). Write a Python program that allows the
user to:
 Enter new diary entries which should always be appended to the file along with the
current date.
 Display all past entries by reading and showing the file content.
 Show the entries in reverse order (latest first) when displaying.
 Count and display the total number of diary entries written by the student.'''
import datetime
def add_diary(filename):
    entry=input("Enter the details ")
    date=datetime.date.today().strftime("%Y-%m-%d")
    with open(filename,"a") as out:
        out.write(f"{date} : {entry}\n")
def view(filename):
    with open(filename,"r") as out:
        contents=out.readlines()
        for line in reversed(contents):
            print(line)
    print("Number of entries ",len(contents))
name=input("Enter the student name ")
filename=name+".txt"
print("1.Add\n2.View\n3.Exit ")
while True:
    ch=int(input("Enter your choice "))
    if ch==1:
        add_diary(filename)
    elif ch==2:
        view(filename)
    else:
        print("Exiting...")
        break
