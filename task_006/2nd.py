for i in range (5):
    if i==0 or i==4:
        for j in range (5):
            print("*", end=" ")
        print("\n")
    else:
        for j in range (5):
            if j==0 or j==4:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print("\n")
