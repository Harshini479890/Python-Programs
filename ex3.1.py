'''1. Pangram is a sentence that uses every alphabet atleast once. Write a function
isPangram() that checks if the given string is a pangram or not. (Return type of
function is Boolean)'''
s=input("Enter the senetence ")
def pangram(s):
    alpha="abcdefghijklmnopqrstuvwxyz"
    for char in alpha:
        if char not in s.lower():
            return False
        return True
if(pangram(s)):
    print(s," is a pangram ")
else:
    print(s," is not a pangram ")
