'''5. Movie Ticket Booking
Description:
A movie theater wants to manage ticket details. Each ticket has a movie name, seat number,
and ticket price. The theater name is common for all tickets.
What to do:
 Create a class named MovieTicket.
 Define instance variables for movie_name, seat_no, and ticket_price.
 Define a class variable for theatre_name.
 Create a constructor to initialize the ticket details.
 Write two methods:
o display_ticket() → Show ticket details.
o update_price(new_price) → Change the ticket price to the new value.
 Create two ticket objects, update the price of one ticket, and display both tickets.'''
class MovieTicket:
    def __init__(self,mname,seatno,tprice):
        self.mname=mname
        self.seatno=seatno
        self.tprice=tprice
    theatren="Anand Complex"
    def display(self):
        print(f"Name : {self.mname}")
        print(f"Seat number : {self.seatno}")
        print(f"Ticket price : {self.tprice}")
        print(f"Theatre name : {MovieTicket.theatren}")
    def update(self,np):
        self.tprice=np
m1=MovieTicket("Dhruva",12,500)
m2=MovieTicket("Orange",24,200)
print("Ticket details ")
m1.display()
m2.display()
np=int(input("Enter the new ticket price "))
print("Ticket details after new ticket price ")
m2.update(np)
m2.display()
