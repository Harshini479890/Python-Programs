'''4. Movie Review Collector
A film club wants to maintain reviews of different movies in a text file called
reviews.txt.
Each line should contain:
MovieName - ReviewerName - ReviewText
Write a Python program that:
 Allows new reviews to be added (appended) to the file.
 Reads and displays all reviews of a particular movie entered by the user.
 Counts and displays the total number of reviews currently in the file.
 Displays how many reviews each movie has received (using counting logic).'''
def add():
    mname=input("Enter movie name ")
    reviewn=input("Enter your name ")
    revt=input("Enter the review about the movie ")
    with open("reviews.txt","a") as out:
        out.write(f"{mname} {reviewn} {revt}\n")
def display():
    with open("reviews.txt","r") as out:
        for line in out:
            mname,reviewn,revt=line.strip().split(' ')
            print(f"Movie Name : {mname} Reviewer Name : {reviewn} Review : {revt}")
def count():
    count=0
    with open("reviews.txt","r") as out:
        for line in out:
            count+=1
    print("Number of reviews ",count)
def disreview():
    count=0
    sm=input("Enter the movie name to find how many reviews it got ")
    with open("reviews.txt","r") as out:
        for line in out:
            mname,reviewn,revt=line.strip().split()
            if sm in mname.lower():
                count+=1
    print("Number of reviews ",count)
while(True):
    print("1.add\n2.display\n3.count\n4.display how many reviews for a movie")
    ch=int(input("Enter your choice "))
    if ch==1:
        add()
    elif ch==2:
        display()
    elif ch==3:
        count()
    elif ch==4:
        disreview()
    else:
        print("Invalid choice ")
        break
