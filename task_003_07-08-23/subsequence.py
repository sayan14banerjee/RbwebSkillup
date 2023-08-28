l = ["sayan", "is", 'good', 'boy']
sub = "y" # this is the specific substring
new = [] # new list to store the specific string
for i in l:
    if sub in i: # check for substring
        new.append(i)
print("The new string is ", new)
