'''3. Hospital Patient Log System
A hospital maintains a daily patient log in a text file named patients.txt. Each entry contains
the patient’s name, age, and reason for visit. Write a program that allows the hospital staff to:
 Append new patient records to the log at the end of the day.
 Display all patient records stored in the file.
 Allow searching by patient name (case-insensitive) to check whether the person has
visited before.
 Count and display how many patients visited for a specific reason (e.g., “Fever”).'''
def add():
    name=input("Enter patients name ")
    age=int(input("Enter patients age "))
    reason=input("Enter the reason to visiy hospital ")
    with open("patients.txt","a") as out:
        out.write(f"{name} {age} {reason}\n")
def display():
    with open("patients.txt","r") as out:
        for line in out:
            print(line)
def search():
    found=False
    sname=input("Enter the patient name u want to search ")
    with open("patients.txt","r") as out:
        for line in out:
            name,age,reason=line.strip().split()
            if sname in name.lower():
                print(f"Name : {name} Age : {age} Reason : {reason}")
                found=True
    if(found):
        print("Visited Before")
    else:
        print("Not visited ")
def count():
    count=0
    sreason=input("Enter a specific reason ")
    with open("patients.txt","r") as out:
        for line in out:
            name,age,reason=line.strip().split()
            if sreason in reason.lower():
                count+=1
    print("Number of patients visited for a specific reason ",reason,"is ",count)

