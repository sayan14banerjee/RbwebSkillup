for i in range (5,0,-1):
    print(" "*(5-i)*2, end=" ")
    for j in range (i+i-1):
        print("*", end=" ")
    print("\n")