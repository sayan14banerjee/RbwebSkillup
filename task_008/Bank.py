class Customer:#Class for user details
    def __init__(self, name, address, age) :
        self.name=name
        self.age = age
        self.address = address
    def info(self):
        print(f"{self.name} is our customer and his age is {self.age}. His address is {self.address}")
class Account:#class for account details
    def __init__(self, account_no, account_type):
        self.account_no = account_no
        self.account_type = account_type
    def info(self):
        print(f"The account number of the user is {self.account_no}  and acount type is {self.account_type}")
class Bank:#class for bank details
    def __init__(self, bname, brname, ifscCode, address) :
        self.bname = bname
        self.brname = brname
        self.ifscCode = ifscCode
        self.address = address
    
    def info(self):
        print(f"The name of thr bank is: {self.bname} \n branch name is: {self.brname} \n and ifsc code: {self.ifscCode} ]\n address: {self.address}")
class Trnsaction:#class for transaction 
    def __init__(self, balance):
        self.balance= balance
    def checkBalance(self ):
        print(f"Bank balance: {self.balance}")
    def withdraw(self, amount):
        self.balance -= amount#decrease balance
        self.checkBalance()
    def deposit(self, amount):
        self.balance += amount#increase balance
        self.checkBalance()
        
def main():
        while(True):
            try:
                #take input abot user and account details
                name = input("Enter customer name: ")
                age= int(input("Enter your age: "))
                address = input("Enter address: ")
                account_no=int(input("enter account no: "))
                account_type=input("Enter your account type:(savings/current) ")
                balance=float(input("Enter your current balance: "))
                #create objects 
                user = Customer(name, address, age)
                uacc = Account(account_no, account_type)
                bank = Bank('SBI', 'Krishnagar-gopinathpur', 'SBI0008', 'Krishnagar')
                trans = Trnsaction(balance)
                if name.isalpha() and address.isalpha() and account_type.isalpha():
                    while(True):
                        try:
                            #take choise from user what he want to do
                            choise=int(input("\nEnter what do you want \n1. See user details\n2. know about user account\n3. details about bank\n4. check bank balance\n5. deposit money\n6 withdraw money\n7. Exit\n"))
                            match choise :
                                case 1:
                                    user.info()#give user information
                                case 2:
                                    uacc.info()#give account details
                                case 3:
                                    bank.info()#give bank details
                                case 4:
                                    trans.checkBalance()#show account balance
                                case 5:
                                    amount = int(input("Enter amount: "))   
                                    trans.deposit(amount)#decrease money  from balance
                                case 6:
                                    while(True):
                                        try:
                                            amount = float(input("Enter amount: "))
                                            if amount > balance :# check given amount is greater os leaa than balance 
                                                print("Insufficient balance.......")#if amount is great than balance show error
                                            else: 
                                                trans.withdraw(amount)#if amount is equal or less than balance 
                                                break
                                        except ValueError:
                                            print("Enter proper amount")
                                case 7:
                                    break
                                case _:
                                    raise ValueError()
                        except ValueError as e:
                            print(e, "Enter valid Input")
                else:
                    raise ValueError()
            except ValueError as e:
                print(e, "Enter valid Input")
            ch=input("Do you want to continue press Y or press any key to exit: ")#to continue for othe user 
            if ch != 'y' and ch !="Y":
                return 

if __name__ == "__main__":
    main()

