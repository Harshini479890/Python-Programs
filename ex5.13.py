'''Q12. OutOfStockError
Create a custom exception OutOfStockError.
Scenario:
 A shopping cart system checks product availability.
 If the requested quantity is more than available stock, raise this exception.'''
class OutOfStockError(Exception):
    def __init__(self):
        super().__init__("Stock not available.")
stock=50
q=int(input("Enter the quantity "))
try:
    if q>stock:
        raise OutOfStockError
    else:
        print("Product available.")
except OutOfStockError as i:
    print(i)
