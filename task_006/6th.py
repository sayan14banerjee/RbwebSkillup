for i in range (1,6):
    print(" "*(6-i)*2, end=" ")
    if i==1 or i== 5:
        for j in range (i):
            print("*", end=" ")
        print("\n")
    else:
        for j in range (i):
            if j==0 or j==i-1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print("\n")