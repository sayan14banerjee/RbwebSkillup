l=[12,65,4,54,54,65,3]
max=l[0]
min=l[0]
for i in l:
    if max<i : #check the max element
        max = i
    if min>i and l.index(max) > l.index(min) : # check the min element which is before the max element
        min = i
print("The maximum difference is {}".format(max-min))