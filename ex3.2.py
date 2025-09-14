'''2. Write a python code that receives a hyphen separated sequence of words as
input. This string is passed as argument to a function convert() that returns the string
as hyphen separated after sorting them alphabetically. (Hint: use split() method)
Eg. Input string: Here-is-the-Great-Wall-of-China
Output: China-Great-Here-Wall-is-of-the'''
s=input("Enter the hyphen seperated sentence ")
def convert(s):
    res=""
    x=s.split('-')
    x.sort()
    for item in x:
        res+=str(item)+'-'
    res=res.strip('-')
    return res
print(convert(s))
