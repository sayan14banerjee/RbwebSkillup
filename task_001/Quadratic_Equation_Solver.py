a = int(input("Enter value of a:"))
b = int(input("Enter value of b:"))
c = int(input("Enter value of c:"))
print(f"The eqiuation is {a}X^2+{b}x+{c}=0")

d=b**2-4*a*c
if d>0:
    print("Two distinct real roots.")
elif d==0:
    print("One real root")
elif d<0:
    print("No real roots.")
else:
    print('Invalid')