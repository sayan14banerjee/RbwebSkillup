l = [12, 12, 21, 54, 46, 87]
n = int(input("Enter the rotate point: "))
l2 = l[n:] + l[:n] # add the last par of list before the first of the list
print("The rotate list is ", l2)
