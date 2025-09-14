'''5. To-Do List Manager
A student wants to keep track of their daily tasks in a text file todo.txt. Each line contains one
task description. Write a program that:
 Appends new tasks entered by the user to the file.
 Displays the complete list of tasks by reading the file.
 Allows the student to search for a keyword (e.g., “exam”) and display only the
matching tasks.
 Provides an option to mark a task as completed (remove it from the file by rewriting
without that task).
 Displays the tasks in alphabetical order for easy viewing.'''
def add():
    task=input("Enter your task ")
    with open("todo.txt","a") as out:
        out.write(f"{task}\n")
def display():
    with open("todo.txt","r") as out:
        for line in out:
            print(line)
def search():
    stask=input("Enter the keyword to search matching tasks and display")
    with open("todo.txt","r") as out:
        for line in out:
            if stask in line:
                print(line)
def remove():
    with open("todo.txt","r") as out:
        lines=out.readlines()
    mtask=input("Enter the task you have done ")
    with open("todo.txt","w") as out:
        for line in lines:
            if mtask not in line:
                out.write(line)
def disalpha():
    with open("todo.txt","r") as out:
        for line in sorted(out):
            print(line)
while(True):
    print("1.add\n2.display\n3.search\n4.remove\n5.display in alphabetical order")
    ch=int(input("Enter your choice "))
    if ch==1:
        add()
    elif ch==2:
        display()
    elif ch==3:
        search()
    elif ch==4:
        remove()
    elif ch==5:
        disalpha()
    else:
        print("Invalid choice")
        break
