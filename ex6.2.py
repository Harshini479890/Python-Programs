'''2. Product Inventory Management
Description:
A store wants to keep track of its products. Each product has a name, price, and quantity
available. The store name is common for all products.
What to do:
 Create a class named Product.
 Define instance variables for product_name, price, and quantity.
 Define a class variable for store_name.
 Create a constructor to initialize the product details.
 Write two methods:
o display_product() → Show product details.
o update_quantity(new_qty) → Update the quantity with a new value.
 Create two product objects, update their quantity using the method, and display the
updated details.'''
class Product:
    storen="XYZ"
    def __init__(self,pname,price,quantity):
        self.pname=pname
        self.price=price
        self.quantity=quantity
    def display_product(self):
        print(f"Store name :{Product.storen},Name : {self.pname},Price : {self.price},Quantity : {self.quantity}")
    def update(self,q):
        self.quantity=q
p1=Product("Soap",125,2)
p1.display_product()
p2=Product("Paste",60,1)
print("Before updation ")
p2.display_product()
q=int(input("Enter the quantity u want to update "))
p2.update(q)
print("After updation ")
p2.display_product()
