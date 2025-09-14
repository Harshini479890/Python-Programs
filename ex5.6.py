'''Q5. AttributeError – Missing Method
Create a program that:
 Reads a string from the user.
 Tries to call a non-existing method (like toUppercase() instead of upper()).
 Handle the exception gracefully.'''
try:
    s=input("Enter a string ")
    su=s.toUppercase()
    print(su)
except AttributeError:
    print("Missing method")
