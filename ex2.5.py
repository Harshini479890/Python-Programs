'''Q5. Write a python code for the following scenario:
A student will not be allowed to sit in exam if his/her attendance is less than
75%.Take the following input from user:- Number of classes held, Number of
classes attended. Compute and print the percentage of class attended and also
print if the student is allowed to sit in exam or not.'''
noch=int(input("Enter the number of classes held "))
noca=int(input("Enter the number of classes attended "))
cap=(noca/noch)*100
if cap<75:
    print("Class attended percentage ",cap)
    print("Not allowed to sit in exam ")
else:
    print("Class attended percentage ",cap)
    print("Allowed to sit in exam ")
