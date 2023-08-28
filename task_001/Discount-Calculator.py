p=input("Enter the price: ")
d=int(input("Enter discpount in percentage: "))
if p.isdigit():
    n=int(p)
    if d>=0 and d<= 100:
        t=n-n*d/100
        print("The total price is: ", t)
    else:
        print("Invalid")

else:
    print("Input invalid")