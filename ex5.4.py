'''Q4. KeyError – Dictionary Lookup
A dictionary contains product codes and prices. Write a program that:
 Takes a product code from the user.
 Displays the price.
 If the product code does not exist, handle the exception and show:
"Invalid product code."'''
mydict={}
n=int(input("Enter number of entries "))
for _ in range(n):
    key=input("Enter key ")
    value=input("Enter value ")
    mydict[key]=value
print(mydict)
pcode=input("Enter the product code ")
try:
    print(mydict[pcode])
except KeyError:
    print("Invalid product code ")
