class Customer:
    def __init__(self, name, address, age) :
        self.name=name
        self.age = age
        self.address = address
    def info(self):
        print(f"{self.name} is our customer and his age is {self.age}. His address is {self.address}")
class Account:
    def __init__(self, account_no, balance, account_type):
        self.account_no = account_no
        self.balance = balance
        self.account_type = account_type
    def info(self):
        print(f"The account number of the user is {self.account_no} and its current balance is {self.balance}$ and acount type is {self.account_type}")
class Bank:
    def __init__(self, B_) :
        pass
class Trnsaction:
    def __init__(self) -> None:
        pass
def main():
    while(True):
        try:
            name = input("Enter customer name")
            age= int(input("Enter your age: "))
            address = input("Enter address: ")
            account_no=int(input("enter account no: "))
            account_type=input("Enter your account type: ")
            balance=float(input("Enter your current balance: "))
            if name.isalpha() and address.isalpha() and account_type.isalpha():
                cust1 = Customer(name, address, age)
                cust1.info()
                acc1 = Account(account_no, balance, account_type)
                acc1.info()
        except ValueError as e:
            print(e, "Enter valid Input")

if __name__ == "__main__":
    main()

