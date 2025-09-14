'''Q6. Write a program to input marks in English, Maths and Science of 10
students who have passed CBSE Examination 2024. Now perform the following
tasks:
a) Print the number of students who have secured 95% or more in all the
subjects.
b) For each subject, print the number of students who have secured 90%
or more.'''
count=0
cme=0
cmm=0
cms=0
for i in range(10):
    print(f"Enter the marks of student {i+1}: ")
    me=int(input("Enter the marks in English "))
    mm=int(input("Enter the marks in Maths "))
    ms=int(input("Enter the marks in Science "))
    per=((me+mm+ms)/300)*100
    if(per>=95):
        count=count+1
    if(me>=90):
        cme=cme+1
    if(mm>=90):
        cmm=cmm+1
    if(ms>=90):
        cms=cms+1
print("Number of students who scored 95% or more are ",count)
print("Number of students who scored 90% or more in English ",cme)
print("Number of students who scored 90% or more in Maths ",cmm)
print("Number of students who scored 90% or more in Science ",cms)
    
