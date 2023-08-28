n=input("Is temperature in (Celsius or Fahrenheit) \nFor Fahrenhite Press F/f and\n For Celcius press C/c : ")
if n=="c ":
    c=int(input('Enter your temp in celcius: '))
    f=(c*9/5) + 32
    print("Your Temp in fahrenheit: ", f)
elif n=="f" :
    f = int(input('Enter your temp in fahrenheit: '))
    c = (f -32) * 5/9
    print("Your Temp in celcius: ", c)
else:
    print("Input invalid")