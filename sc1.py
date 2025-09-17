'''1. Encapsulation with Getters and Setters
Problem 1: Bank Account Management System
You are building a banking system where customers can open accounts and manage
their transactions.
Create a class BankAccount that:
- Has private attributes:
- __account_number (string)
- __balance (float, default = 0.0)
- Provides the following features:
- Deposit method: Adds money to the account (only positive amounts allowed).
- Withdraw method: Deducts money if sufficient balance exists; otherwise, display
'Insufficient Funds'.
- Getter and Setter for balance:
- Getter returns current balance.
- Setter ensures the balance cannot be negative.
- Use __str__ to print account details in the format:
Account Number: 12345 | Balance: ₹5000.0'''
class InsufficientFunds(Exception):
    def __init__(self):
        super().__init("Balance is less than withdraw amount.")
class BankAccount:
    def __init__(self,acno,bal=0.0):
        self.__acno=acno
        self.__bal=bal
    def getbal(self):
        return self.__bal
    def setbal(self,bal):
        if bal>=0:
            self.__bal=bal
        else:
            print("Balance is negative.")
    def dep(self,amt):
        if amt>0:
            self.__bal+=amt
        else:
            print("Amount is negative.")
    def withdraw(self,amt):
        try:
            if self.__bal<amt:
                raise InsufficientFunds
            else:
                self.__bal-=amt
        except InsufficienFunds as i:
            print(i)
    def __str__(self):
        return f"Account Number: {self.__acno} | Balance: {self.__bal}"
if __name__=="__main__":
    b1=BankAccount("12345",5000.0)
    while(True):
        print("1.Deposit\n2.Withdraw\n3.Show\n4.Exit")
        ch=int(input("Enter your choice "))
        if ch==1:
            amt=float(input("Enter the deposit amount "))
            b1.dep(amt)
            print("Balance : ",b1.getbal())
        elif ch==2:
            amt=float(input("Enter the withdraw amount "))
            b1.withdraw(amt)
            print("Balance : ",b1.getbal())
        elif ch==3:
            print(b1)
        elif ch==4:
            print("Exiting..")
            break
        else:
            print("Invalid choice.")
