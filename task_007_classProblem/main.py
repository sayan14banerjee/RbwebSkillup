class Teachers: #class for all teachers
    def __init__(self, name, age, salary, experience, depertment): #construtor fuction 
        self.name = name
        self.age = age
        self.salary = salary
        self.increament=.5
        self.experience= experience
        self.depertment= depertment

    def info(self): #teachers details
        print(f"The name of Teacher is {self.name}, and his age is {self.age} years")

    def presentSalary(self): #get salary info
        print(f"{self.name}'s salary is {self.salary}")

    def increase(self): # incraesee salary of teachers
        self.salary=int(self.salary+(self.salary*self.increament))# salary increase by increament 
        print(f"Now salary is {self.salary}")
    
    def workProfile(self): # get info about teachers experience and teaching field
        print(f"{self.name} has {self.experience} year experince \n he works in {self.depertment}")

    def retire(self):#check for retirement
        if self.age >60:
            print("You can retire now ")
            self.salary=0
            self.presentSalary()
        else:
            print ("you are not eligible to retire yet")

class Students:#class for all students
    def __init__(self, name , age, department, sem, phNo, email ):#construtor fuction 
        self.name = name
        self.age = age
        self.depertment = department
        self.phNo  = phNo
        self.email = email
        self.sem = sem
    
    def info(self): #students details
        print(f"Name of the stuent is {self.name} and age is {self.age} years")

    def contact(self):#students contact
        print(f"Contact details are : {self.phNo}, {self.email}")
    
    def studyDetails(self):# students depertment and sem 
        print(f"{self.name} is study in {self.sem} sem in {self.depertment}")

    def changeDepertment(self): #change depertment 
        newDept = input("Enter new depertment: ")
        self.depertment = newDept
        print(f"{self.name} is now in {self.depertment}")
    
    def applyForLeave(self):
        self.name = None
        self.age = None
        self.depertment = None
        self.phNo  = None
        self.email = None
        self.sem = None

        print("You can leave our institute")

class NonTeachingStaff:#class for all non teaching staff
    def __init__(self, name, age, salary, workingYears):
        self.name = name
        self.age = age
        self.salary = salary
        self.increament= .2
        self.workingYears= workingYears

    def info(self): #non teaching staff details
        print(f"The name of staff is {self.name}, and his age is {self.age} years")

    def presentSalary(self):#get salary info
        print(f"{self.name}'s salary is {self.salary}")

    def increase(self):# incraesee salary of Non teaching staff
        self.salary=int(self.salary*self.increament)# salary increase by increament 
    
    def workProfile(self): # get info about nonteaching staff work
        print(f"{self.name} is working for {self.workingYears} years. ")
    
    def retire(self):#check for retirement
        if self.age >60:
            print("You can retire now ")
            self.salary=0
            self.presentSalary()
        else:
            print ("you are not eligible to retire yet")
    
def main():
    while(True):# to continue the program until the user don't want to exit
        try:# for take input only integer value from user of class number
            classNo = int(input("\n\nEnter class no  \n 1. Teachers \n 2.Students \n3.  Non teaching staff \npress 1/2/3 or press 4 to exit: "))
            match classNo:#match case to give access of classes of the class to user accroding his require
                case 1:
                    try:
                        print("\nYou are in Teacher section..")
                        #input from user about teacher
                        name = input("Enter name of teacher: ")
                        age = int(input("Enter age of teacher: "))
                        salary = int(input("Enter the salary of teacher: "))
                        exp = int(input("Enter the experience of eacher: "))
                        dept= input("Enter the depertment of teacher: ")
                        if name.isalpha() and dept.isalpha():
                            teacher1 =Teachers(name, age, salary, exp, dept)
                            while(True):
                                try:# for take input only integer value from user of class number
                                    functionNo = int (input("\nEnter function no  \n 1. Info \n 2.work profile \n3.  present salary \n4. Increase salary \n5.retire check \npress 1/2/3/4/5 or press 6 to exit: "))
                                    match functionNo: #match case to give access of fuction of the class to user accroding his require
                                        case 1:
                                            teacher1.info()
                                        case 2:
                                            teacher1.workProfile()
                                        case 3:
                                            teacher1.presentSalary()
                                        case 4:
                                            teacher1.increase()
                                        case 5:
                                            teacher1.retire() 
                                        case 6:
                                            break
                                        case _:
                                            raise ValueError()# Create error if input is not satisfied 
                                except ValueError:
                                    print("Press only 1/2/3/4/5....../n")
                        else :
                             raise ValueError()#if name and dept contain numeric value it occurs errror
                    except ValueError:
                                    print("Invalid input...Please enter proper input......")  
                case 2:
                    try: 
                        print("\nYou are in Students section..")
                        #input from user about teacher
                        name = input("Enter name of students: ")
                        age = int(input("Enter age of students: "))
                        dept= input("Enter the depertment of teacher: ")
                        sem = int(input("Enter the sem of student: "))
                        ph = int(input("Enter the phone number of students: "))
                        email = input("Emnter the email id: ")
                        if name.isalpha() and dept.isalpha():
                            student1 = Students(name, age, dept, sem, ph, email)
                            while(True):
                                try:# for take input only integer value from user of function number
                                    functionNo = int (input("\nEnter function no  \n 1. Info \n 2.study details \n3. contacts \n4. change depertment \n5. aply for leave \npress 1/2/3/4/5 or press 6 to exit: "))
                                    match functionNo:#match case to give access of fuction of the class to user accroding his require
                                        case 1:
                                            student1.info()
                                        case 2:
                                            student1.studyDetails()
                                        case 3:
                                            student1.contact()
                                        case 4:
                                            student1.changeDepertment()
                                        case 5:
                                            student1.applyForLeave()
                                        case 6:
                                            break
                                        case _:
                                            raise ValueError()# Create error if input is not satisfied
                                except ValueError:
                                    print("Press only 1/2/3/4/5.....")
                        else :
                             raise ValueError()#if name and dept contain numeric value it occurs errror
                    except ValueError:
                                    print("Invalid input...Please enter proper input......")  
                case 3:
                    try:
                        print("\nYou are in No Teaching staff section..")
                        #input from user about teacher
                        name = input("Enter name of teacher: ")
                        age = int(input("Enter age of teacher: "))
                        salary = int(input("Enter the salary of teacher: "))
                        exp = int(input("Enter the experience of eacher: "))
                        if name.isalpha() and dept.isalpha():
                            nonTeacher1 =NonTeachingStaff(name, age, salary, exp)
                            while (True):
                                try:# for take input only integer value from user of function number
                                    print("\nYou are in Non teaching staff section..")
                                    functionNo = int (input("\nEnter function no  \n 1. Info \n 2.work profile \n3.  present salary \n4. Increase salary \npress 1/2/3/4/5 or press 6 to exit: "))
                                    match functionNo:#match case to give access of fuction of the class to user accroding his require
                                        case 1:
                                            nonTeacher1.info()
                                        case 2:
                                            nonTeacher1.workProfile()
                                        case 3:
                                            nonTeacher1.presentSalary()
                                        case 4:
                                            nonTeacher1.increase()
                                        case 5:
                                            nonTeacher1.retire()
                                        case 6:
                                            break
                                        case _:#default 
                                            raise ValueError()# Create error if input is not satisfied
                                except ValueError :
                                        print("Invalid input Press only 1/2/3/4/5 or 6......\n")
                        else :
                             raise ValueError()#if name and dept contain numeric value it occurs errror
                    except ValueError:
                                    print("Invalid input...Please enter proper input......") 
                case 4:
                    return
                
                case _:
                    raise ValueError('Invalid Input')# Create error if input is not satisfied
        except ValueError:
            print("Enter only 1/2/3/4..... \n \n")


if __name__=="__main__":
    main()
