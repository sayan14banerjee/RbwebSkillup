n=int(input("Enter the range of the prime number: "))
#check n number using a while loop and a for loop
print(f"First {n} prime number")
i=0
while(i<=n):
    prime=True
    #Check is prime
    if (i>1):
        for j in range(2,i//2+1):
            if((i%j)==0):
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
        print(f"{i} is prime")
    i+=1