#using inheritence
class Customer:#Class for user details
    def __init__(self, name, address, age, bal, accno) :
        self.name=name
        self.age = age
        self.address = address
        self.bal = bal
        self.accno= accno
    def info(self):
        print(f"{self.name} is our customer and his age is {self.age}. His address is {self.address}")
    def acc(self):
               print(f"account no {self.accno}")
    def balance(self): 
              print(f" His balance is {self.bal}")
    def balinc(self,amount):
         self.bal += amount
    def baldec(self,amount):
         self.bal -= amount
class Account (Customer): #Inheriting from class customer
        def __init__(self, acc_type, name, address, age, bal, accno):
            super().__init__(name, address, age, bal, accno)
            self.acc_type = acc_type
        def dtl(self):
              print(f"Account type: {self.acc_type}")
              super().acc()
              super().balance()
class Bank:#class for bank details
    def __init__(self, bname, brname, ifscCode, address) :
        self.bname = bname
        self.brname = brname
        self.ifscCode = ifscCode
        self.address = address
    def info(self):
            print(f"The name of thr bank is: {self.bname} \n branch name is: {self.brname} \n and ifsc code: {self.ifscCode} ]\n address: {self.address}")

class Transfer(Customer):
        def __init__(self, name, address, age, bal, accno):
            super().__init__(name, address, age, bal, accno)
            
        
        def tran(self, amount, tacc):
              print(f"Amount Rs.{amount} is transferd to {tacc}")
              super().baldec(amount)
              super().balance()
class Withdraw(Customer):
        def __init__(self, name, address, age, bal, accno):
            super().__init__(name, address, age, bal, accno)
        def wd(self, amount):
              print(f"Amount Rs.{amount} is Debit")
              super().baldec(amount)
              super().balance()
class Deposit(Customer):
        def __init__(self, name, address, age, bal, accno):
            super().__init__(name, address, age, bal, accno)
        def dep(self, amount):
              print(f"Amount Rs.{amount} is Credit")
              super().balinc(amount)
              super().balance()
      
def main():
       while(True):
            try:
                #take input abot user and account details
                name = input("Enter customer name: ")
                age= int(input("Enter your age: "))
                address = input("Enter address: ")
                account_no=int(input("enter account no: "))
                account_type=input("Enter your account type:(savings/current) ")
                balance=int(input("Enter your current balance: "))
                #create objects 
                user = Customer(name, address, age, balance, account_no)
                uacc = Account(account_type, name, address, age, balance, account_no)
                bank = Bank('SBI', 'Krishnagar-gopinathpur', 'SBI0008', 'Krishnagar')
                trans = Transfer(name, address, age, balance, account_no)
                withdraw = Withdraw(name, address, age, balance, account_no)
                deposit = Deposit(name, address, age, balance, account_no)
                #print menu options
                if name.isalpha() and address.isalpha() and account_type.isalpha():
                    while(True):
                        try:
                            #take choise from user what he want to do
                            choise=int(input("\nEnter what do you want \n1. See user details\n2. know about user account\n3. details about bank\n4. check bank balance\n5. deposit money\n6 withdraw money\n7. transfer money \n8. Exit\n"))
                            match choise :
                                case 1:
                                    user.info()#give user information
                                case 2:
                                    uacc.dtl()#give account details
                                case 3:
                                    bank.info()#give bank details
                                case 4:
                                    user.balance()#show account balance
                                case 5:
                                    amount = int(input("Enter amount: "))   
                                    deposit.dep(amount)#decrease money  from balance
                                case 6:
                                    while(True):
                                        try:
                                            amount = float(input("Enter amount: "))
                                            if amount > balance :# check given amount is greater os leaa than balance 
                                                print("Insufficient balance.......")#if amount is great than balance show error
                                            else: 
                                                withdraw.wd(amount)#if amount is equal or less than balance 
                                                break
                                        except ValueError:
                                            print("Enter proper amount")
                                case 7:
                                    while(True):
                                        try:
                                            amount = float(input("Enter amount: "))
                                            tacc = int(input("Enter account no :"))
                                            if amount > balance :# check given amount is greater os leaa than balance 
                                                print("Insufficient balance.......")#if amount is great than balance show error
                                            else: 
                                                trans.tran(amount, tacc)#if amount is equal or less than balance 
                                                break
                                        except ValueError:
                                            print("Enter proper amount")
                                case 8:
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