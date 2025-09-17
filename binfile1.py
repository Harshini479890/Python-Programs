import pickle
def writer(filename):
    n=int(input("Enter number of students: "))
    stud=[]
    for i in range(n):
        rno=int(input("Enter rollno "))
        name=input("Enter name ")
        marks=int(input("Enter marks "))
        stud.append((rno,name,marks))
    with open(filename,"wb") as f:
        pickle.dump(stud,f)
def reader(filename):
    with open(filename,"rb") as f:
        stud=pickle.load(f)
    for s in stud:
        print(f"Rollno: {s[0]}| Name: {s[1]} | Marks: {s[2]}")
filename="students.dat"
writer(filename)
reader(filename)
