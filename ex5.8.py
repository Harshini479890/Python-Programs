'''Q7. Bank Withdrawal Scenario – A bank system allows customers to withdraw money.
Write a program that:
 Takes account balance and withdraw amount as input.
 If the withdraw amount is greater than the balance, raise a custom exception
InsufficientFundsError with the message:
"Transaction failed: Withdrawal amount exceeds available balance."
 Otherwise, print the updated balance.
Hint: Define a custom exception class InsufficientFundsError and raise it when necessary.'''
class InsufficientFundsError(Exception):
    def __init__(self):
        super().__init__("Insufficient Balance ")
def amt():
    ab=int(input("Enter the account balance "))
    wa=int(input("Enter the withdraw amount "))
    try:
        if wa>ab:
            raise InsufficientFundsError
        else:
            ab=ab-wa
            print("Account Balance ",ab)
    except InsufficientFundsError as i:
        print(i)
amt()
