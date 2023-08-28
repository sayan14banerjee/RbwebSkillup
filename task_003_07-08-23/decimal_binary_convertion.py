choise = input("Which conversion you want \n press b for binary to decimal \n press d for decimal to binary ")
if choise == 'b': # bnary to decimal 
    n = (input("Enter the number in binary : "))
    pow = int(len(n) - 1)
    sum = 0
    for i in n:
        if i not in {'0', '1'}: # check the input is binary or not
            print('Enter only 1 or 0')
            break
        else:
            sum += int(i) * 2 ** pow # it calculate the decimal

        pow -=1
    print(f"THe binary of {n} is {sum}")
elif choise == 'd': # dcimal to binary
    n = int(input("Enter the number in decimal: "))
    l=[]
    while(n > 0):
        r = n % 2
        n = n // 2
        l.insert(0, r) #add the binary number in list 
    print(f"The binary of the number is {l}")
else: 
    print("ENter only b or d")