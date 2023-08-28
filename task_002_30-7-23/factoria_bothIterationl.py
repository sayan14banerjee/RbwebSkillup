n=input("Enter a number: ")
#converting string to integer using int() function and storing it in variable 'x'
x=int(n)
fact=1
if x > 0 : #posetive number
    #using for loop
    for i in range (x, 0, -1):
        fact=fact*i
elif x==0:
    print("The factorial of 0 is 0")
else: #for negfetive number
    #using while loop
    i=x
    while(i<0):
        fact=fact*i
        i+=1
print("The factorial of {} is {}.".format(x, fact))


