n=int(input("Enter a number : "))
i=0
a=0
b=1
print(f"THe first {n} fibbonacci series number is: {a}, {b}")
while(i<n):
    temp=a+b
    a=b
    b=temp
    print(", ", temp)
    i+=1