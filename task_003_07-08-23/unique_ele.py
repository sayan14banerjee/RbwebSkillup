l = [321, 3241, 321, 321, 354, 654, 987, 654]
l2= [] # list to store unique value
for i in l:
    if i not in l2: # check for duplicate
        l2.append(i)
print("The list with unique elements ", l2)