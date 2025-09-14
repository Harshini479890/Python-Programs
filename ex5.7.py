'''Q6. StopIteration – Manual Iteration
Write a program that:
 Creates an iterator for a list of numbers.
 Uses next() in a loop to display elements.
 When the iterator is exhausted, handle the StopIteration exception and display "End of
list reached."'''
l=[1,2,3,4,5]
iterator=iter(l)
while True:
    try:
        ele=next(iterator)
        print(ele)
    except StopIteration:
        print("End of list reached.")
        break
