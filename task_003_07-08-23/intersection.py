l1 = [12, 321, 32, 469, 987, 65]
l2 = [12, 54, 321, 987, 5465, 321]
l3=[] # intersection list
#chek the long list for keep duplicates
if len(l1) > len(l2):
    for i in l1:
        if i in l2: # check for common
            l3.append(i)
else:
    for i in l2:
        if i in l1: # check for common
            l3.append(i)
print("THe intersection list is: ", l3)
