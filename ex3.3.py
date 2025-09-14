'''3. Write a function create_Sentence() that receives 3 lists of strings as input and
forms sentences by picking up the strings from the 3 lists. All the lists should contain
equal number of strings.
Test case:
Input:
List1 = [‘I’, ‘We’]
List2 = [‘want’, ‘create’]
List3 = [‘justice’, ‘peace’]
Output:
I want justice
We want justice
I want peace
We want peace
I create justice
We create justice
I create peace
We create peace'''
l1=input("Enter 2 strings of list 1 ").split()
l2=input("Enter 2 strings of list 2 ").split()
l3=input("Enter 2 strings of list 3 ").split()
def create_sentence(l1,l2,l3):
    for item1 in l1:
        for item2 in l2:
            for item3 in l3:
                print(f"{item1} {item2} {item3}")
create_sentence(l1,l2,l3)
