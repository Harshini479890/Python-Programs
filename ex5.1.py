'''Q1. File Handling Scenario – A company stores its employee details in a text file named
employees.txt. Write a program that:
 Asks the user for the filename.
 Tries to open the file and read its contents.
 If the file does not exist, handle the exception and print:
"Error: The file you are trying to open does not exist."
 If the file is found, print the contents.
Hint to students: Use try-except and handle FileNotFoundError.'''
def openfile(filename):
    try:
        with open(filename,"r") as f:
            for line in f:
                print(line)
    except FileNotFoundError:
        print("Could not find the file named " + filename)
fname=input("Enter the filename: ")
filename=fname+".txt"
openfile(filename)
