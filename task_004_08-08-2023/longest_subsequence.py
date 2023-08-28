l=[1, 8, 2, 5, 3, 9, 12, 15, 4, 10, 13, 14]

l.sort()
print(l)

l1=l[:5]
l2=l[5:8]
l3=l[8:]

if len(l1) > len(l2) and len(l1) > len(l3):
    print(f"{l1} is the longest")
elif len(l2) > len(l1) and len(l2) > len(l3):
    print(f"{l2} is the longest")
elif len(l3)> len(l1) and len(l3) > len(l2):
    print(f"{l3} is the longest")
else :
    print("The len of subsequence are same")