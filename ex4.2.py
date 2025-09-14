'''2. Library Book Records
A library maintains a text file books.txt where each line contains the book’s
title, author, and year of publication separated by commas. Write a Python
program that:
 Adds a new book record (append mode).
 Displays all books published after the year 2015 (read mode).
 Allows searching for books by a particular author name (case-insensitive).
 Displays the complete list of books in alphabetical order by title.'''
def add_book():
    title=input("Enter the title of the book: ")
    author=input("Enter the book author: ")
    yop=int(input("Enter the year of publication: "))
    with open("books.txt","a") as out:
            out.write(f"{title},{author},{yop}\n")
def displayafter():
    with open("books.txt","r") as out:
        for line in out:
            title,author,yop=line.strip().split(',')
        if int(yop) > 2015:
            print(f"Title : {title}  Author : {author}  Yop: {yop}")
def search():
    bookaut=input("Enter the author name u want to search ")
    with open("books.txt","r") as out:
        for line in out:
            title,author,yop=line.strip().split(',')
            if bookaut in author.lower():
                print(f"Title : {title}  Author : {author}  Yop: {yop}")
def displayall():
     with open("books.txt","r") as out:
        for line in out:
            title,author,yop=line.strip().split(',')
            print(f"Title : {title}  Author : {author}  Yop: {yop}")
while True:
    ch=int(input("Enter your choice\n1.Add book record\n2.Display(2015)\n3.search\n4.Displayall\n "))
    if ch==1:
        add_book()
    elif ch==2:
        displayafter()
    elif ch==3:
        search()
    elif ch==4:
        displayall()
    else:
        print("Exiting...")
        break
            
