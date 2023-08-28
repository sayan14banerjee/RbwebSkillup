for i in range (5, 0, -1):
    print(" "*i, end=" ")
    if i==5 or i==1:
        print("* "*5)
        print('\n')
    else:
        for j in range (5):
            if j==0 or j==4:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print("\n")
    
    