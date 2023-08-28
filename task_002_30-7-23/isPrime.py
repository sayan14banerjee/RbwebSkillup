n=input("Enter a number: ")
#check the input is only integer 
if n.isdigit():
    #converting string to integer using int() function and storing it in variable 'x'
    x=int(n)
    prime=True
    #Check is prime
    if (x>1):
        for i in range(2,x//2+1):
            if((x%i)==0):
                prime=False
                break
            else:
                pass
    else:
        prime=True
        # negative integers can not be prime.
        # 0 and 1 both are not a prime numbe
    #prime or not
    if prime:
        print(f"{x} is prime")
    else:
        print(f"{x} is not prime")
else:
    print("Invalid input enter only integer value")

