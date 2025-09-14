'''Q11. InvalidEmailError
Create a custom exception InvalidEmailError.
Scenario:
 A registration form accepts an email.
 If the email does not contain "@" or ".", raise the exception.'''
class InvalidEmailError(Exception):
    def __init__(self):
        super().__init__("Please enter valid email.")
em=input("Enter your email ")
try:
    if '@' not in em or '.' not in em:
        raise InvalidEmailError
    else:
        print("Valid email : ",em)
except InvalidEmailError as i:
    print(i)
            
