'''Q3. TypeError – Incorrect Data Type
You are creating a program that multiplies two numbers.
 Take two inputs from the user.
 Convert only one of them to an integer and forget the other.
 If multiplication fails due to type mismatch, handle the exception.'''
try:
    a=int(input("Enter number 1: "))
    b=input("Enter number 2: ")
    c=a*b
    print("Product ",c)
except TypeError:
    print("Error: Multiplication failed due to a type mismatch.")
    print("One of the inputs was converted to an integer, while the other remained a string.")
    print("Python cannot perform multiplication between an integer and a string in this manner.")
