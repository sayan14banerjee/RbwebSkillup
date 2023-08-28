l = [("Sayan", 12), ("Shyam", 29), ("Rahul", 22), ("Asif", 25)]
# bubllee sort
for i in range(len(l)):
    for j in range(len(l)-i-1):
        if l[j][1] > l[j+1][1]: #compare only age 
            l[j], l[j+1] = l[j+1], l[j] #change every item of list 

print(l)