try:
    n = int(input("Enter a number "))
    print("square of",n ,"is",n**2)
except ValueError as v:
    print(v, "\nPlease try again ")