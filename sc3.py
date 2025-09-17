'''Problem 3: Online Shopping Cart
Create a ShoppingCart class for an e-commerce platform that:
- Has a private attribute:
- __items (a list of tuples: (item_name, price))
- Provides the following features:
- add_item() → Adds an item to the cart, but does not allow duplicates.
- remove_item() → Removes an item if it exists.
- get_total_price() → Returns the sum of all item prices.
- Print cart details using __str__:
Items in Cart: Apple, Mango | Total Price: ₹150.0'''
class ShoppingCart:
    def __init__(self):
        self.__items=[]
    def add_item(self,iname,price):
        for item in self.__items:
            if item[0]==iname:
                print(f"{iname} is already in the cart.")
                return
        self.__items.append((iname,price))
        print(f"{iname} added to the cart.")
        #print(repr(self.__items))
    def remove_item(self,iname):
        for item in self.__items:
            if item[0]==iname:
                self.__items.remove(item)
                print(f"{iname} removed from the cart.")
                return        
        print("Item not found.")
    def gettotal(self):
        sum=0
        for item in self.__items:
            sum+=item[1]
        return sum
    def __str__(self):
        names=[]
        for item in self.__items:
            names.append(item[0])
        ilist=",".join(names)
        tp=self.gettotal()
        return f"Items in Cart: {ilist} | Total Price: {tp}"
if __name__=="__main__":
    c1=ShoppingCart()
    c1.add_item("Apple",50)
    c1.add_item("Orange",25)
    c1.add_item("Banana",10)
    print(c1)
    c1.remove_item("Apple")
    print(c1)
    c1.remove_item("Pineapple")
    print(c1)
