n=input("Enter a number: ")
#converting string to integer using int() function and storing it in variable 'x'
x=int(n)
fact=1
if x > 0 : #posetive number
    i=x
    while(i>0):
        fact=fact*i
        i-=1
elif x==0:
    print("The factorial of 0 is 0")
else: #for negfetive number
    i=x
    while(i<0):
        fact=fact*i
        i+=1
print("The factorial of {} is {}.".format(x, fact))
