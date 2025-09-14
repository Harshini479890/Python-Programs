'''Q3. IndexError – Accessing List
A company stores employee names in a list. Write a program that:
 Takes an index number from the user.
 Prints the employee at that index.
 Handle the case when the index is out of range.'''
l=input("Enter the names of employees ").split()
index=int(input("Enter the index "))
try:
    print(l[index])
except IndexError:
    print("Index is out of range.")
