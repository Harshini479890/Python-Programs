'''Q8. Age Verification for Movie Booking – A movie booking system allows only users aged
18 and above to book tickets for an adult-rated movie.
Write a program that:
 Takes the user's age as input.
 If the age is less than 18, raise a custom exception UnderAgeError with the message:
"Booking failed: You must be at least 18 years old to watch this movie."
 If age is valid, print:
"Booking successful! Enjoy your movie."
Hint: Define UnderAgeError as a custom exception and use it in the program.'''
class UnderAgeError(Exception):
    def __init__(self):
        super().__init__("Booking failed: You must be at least 18 years old to watch this movie.")
age=int(input("Enter yor age "))
try:
    if age<18:
        raise UnderAgeError
    else:
        print("Booking successful! Enjoy your movie.")
except UnderAgeError as u:
    print(u)
    
    
