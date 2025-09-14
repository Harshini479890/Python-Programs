'''5. Explore the built-in functions of python and demonstrate their functioning with
examples.
abs(), all(), any(), ascii(), bin(), bool(), bytearray(), bytes(), chr()
dict(), dir(), enumerate(), eval() , exec(), filter(), float(), format()
help(), hex(), id(), input(), int(), iter(), len(), list(), max(), min()
next(), object(), oct(), open(), ord(), pow(), print(), property()
range(), repr(), reversed(), round(), set(), slice(), sorted(), str()
sum(), super(), tuple(), type(), vars(), zip()'''
print("Absolut value of -5 is ",abs(-5)) #Returns the absolute value of a number
#all(): Returns True if all elements of an iterable are true
#(or if the iterable is empty).
print(all([True,True,1]))
print(all([True,False]))
#any(): Returns True if any element of an iterable is true.
print(any([True, False]))  # Output: True
print(any([0, False]))    # Output: False
print(ascii('a'))
#bin():Converts an integer to a binary string prefixed with "0b"
print("Bin ",bin(10))
print("Bool ",bool(0))
print("Bool ",bool("abcd"))
#bytearray
arr=bytearray(b'hello')
arr[0]=72
print("Byte array ",arr) #h changes to H
#bytes
b=bytes([65,66,67])
print("Bytes ",b)
print("Character of ascii value of 97 is ",chr(97))
#dict() : creates a new dictionary
d=dict(name="Har",age=19)
print("Created dictionary ",d)
#dir()
print("List of name in the current scope ",dir([]))
#enumerate(): adds a counter to an iterable
print("Enumerate ")
for i,item in enumerate(['a','b']):
    print(i,item)
#eval(): Evaluates a string as a Python expression.
print("eval() ")
x = 10
print(eval('x + 5')) # Output: 15
print("exec() - Executes python code dynamically ")
code="print('Hello from exec')"
exec(code)
print("filter(): Constructs an iterator from elements of an iterable for which a function returns true.")
numbers = [1, 2, 3, 4, 5]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens) # Output: [2, 4]
print("float(): Converts a string or number to a floating-point number.")
print(float("3.14")) # Output: 3.14
print("format(): Formats a value into a formatted representation.")
print(format(123, '05d')) # Output: 00123
print("help(): Invokes the built-in help system.")
# help(print) # Displays documentation for the print function
print("hex(): Converts an integer to a hexadecimal string prefixed with ")
print(hex(255)) # Output: 0xff
print("id(): Returns the identity of an object (its memory address).")
a = 10
print(id(a)) # Output: (a unique integer)
print("input(): Reads a line from input, converts it to a string, and returns it.")
# name = input("Enter your name: ")
# print("Hello, " + name)
print("int(): Converts a string or number to an integer.")
print(int("123")) # Output: 123
print("iter(): Returns an iterator object.")
my_list = [1, 2]
my_iter = iter(my_list)
print(next(my_iter)) # Output: 1
print("len(): Returns the length (the number of items) of an object.")
print(len("Python")) # Output: 6
print("list(): Creates a new list.")
l = list("abc")
print(l) # Output: ['a', 'b', 'c']
print("max(): Returns the largest item in an iterable or the largest of two or more arguments.")
print(max([1, 5, 2])) # Output: 5
print("min(): Returns the smallest item in an iterable or the smallest of two or more arguments.")
print(min([1, 5, 2])) # Output: 1
print("next(): Retrieves the next item from an iterator.")
my_iter = iter([1, 2])
print(next(my_iter)) # Output: 1
print("object(): Returns a new featureless object.")
obj = object()
print(type(obj)) # Output: <class 'object'>
print("oct(): Converts an integer to an octal string prefixed with .")
print(oct(8)) # Output: 0o10
print("open(): Opens a file and returns a file object.")
# with open("example.txt", "w") as f:
#   f.write("Hello")
print("ord(): Returns the integer Unicode code point of a character.")
print(ord('a')) # Output: 97
print("pow(): Returns base raised to the power of exp.")
print(pow(2, 3)) # Output: 8
print("print(): Prints objects to the text stream file, separated by sep and followed by end.")
print("Hello", "World") # Output: Hello World
print("range(): Returns a sequence of numbers.")
for i in range(3):
    print(i)
    # Output:
    # 0
    # 1
    # 2
print("repr(): Returns a string containing a printable representation of an object.")
print(repr('hello')) # Output: 'hello'
print("reversed(): Returns a reverse iterator.")
print(list(reversed([1, 2, 3]))) # Output: [3, 2, 1]
print("round(): Rounds a number to a given precision in decimal digits.")
print(round(3.14159, 2)) # Output: 3.14



