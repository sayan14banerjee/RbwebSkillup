for i in range (1,6):
    print(" "*(5-i)*2, end=" ")
    if i==0 or i==5:
        for j in range (i+i-1):
            print("*", end=" ")
        print("\n")
    else:
        for j in range (i+i-1):
            if j==0 or j==i+i-1-1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print("\n")