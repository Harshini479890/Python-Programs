'''4. Vehicle Details System
Description:
A vehicle showroom needs to manage details of vehicles. Each vehicle has a name, model,
and price. All vehicles belong to the same manufacturer.
What to do:
 Create a class named Vehicle.
 Define instance variables for vehicle_name, model, and price.
 Define a class variable for manufacturer.
 Create a constructor to initialize the vehicle details.
 Write two methods:
o show_details() → Display vehicle details.
o apply_discount(percent) → Reduce the price by the given percentage and
update it.

 Create two vehicle objects, apply discount on both, and display the updated details.'''
class Vehicle:
    def __init__(self,name,model,price):
        self.name=name
        self.model=model
        self.price=price
    man="TM motors"
    def show(self):
        print(f"Name : {self.name}")
        print(f"Model : {self.model}")
        print(f"Price : {self.price}")
        print(f"Manufacturing company : {Vehicle.man}")
    def apply(self,dp):
        self.price=self.price-(dp/100)
v1=Vehicle("Car","Maruti Suzuki",10000000)
v2=Vehicle("Scooti","Bullet",7000000)
print("Vehicle details ")
v1.show()
v2.show()
dp=int(input("Enter the discount in percentage : "))
print("After applying dicount ")
v1.apply(dp)
v2.apply(dp)
v1.show()
v2.show()
