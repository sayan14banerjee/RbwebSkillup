n=input("Enter a number: ")
if n.isdigit():
    x=int(n)
    if x%2==0:
        print(f"{n} is Even")
    else :
        print(f"{n} is odd")
else:
    print("Input invalid")

