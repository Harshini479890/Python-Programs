'''Q9. Negative Stock Error
Create a custom exception NegativeStockError.
Scenario:
 A store keeps track of stock for a product.
 If a user enters a negative stock value while
updating inventory, raise this exception.'''
class NegativeStockError(Exception):
    def __init__(self):
        super().__init__("You have enetered negative stock value please enter a positive value.")
stock=int(input("Enter the stock value "))
try:
    if stock<0:
        raise NegativeStockError
    else:
        print(stock)
except NegativeStockError as i:
    print(i)
