x=input('Enter The year')
if x.isdigit():
    year=int(x)
    if len(x) == 4 and year >0:
        if year %4 == 0 and year %100 != 0 or year % 400 ==0:
            print("Leap year ")
        else:
            print("Common Year")
    else :
        print("invalid year")

else:
    print("Input Invalid")