'''Q7. Get input of n integers from the user one by one and print the number of positive,
negative and zeros. Also find the sum and average of all positive and negative
numbers separately.'''
n=int(input("Enter the number of integers "))
pl=[]
nl=[]
zl=[]
print("Enter the integers one by one ")
for i in range(n):
    cn=int(input("Enter the integer "))
    if(cn>0):
        pl.append(cn)
    elif (cn<0):
        nl.append(cn)
    else:
        zl.append(cn)
print("Number of positive integers ",len(pl))
print("Number of negative integers ",len(nl))
print("Number of zeroes ",len(zl))
print("Sum of positive integers ",sum(pl))
print("Sum of negative integers ",sum(nl))
