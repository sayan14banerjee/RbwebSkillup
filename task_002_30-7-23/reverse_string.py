s=input("Enter a string")
w=""
#reverse using for loop
for i in s:
    if(i.isalpha()):
        w= i+ w
    else:
        print(f"THe numaric value{i} will be clipp")
print (w)
#reverse using while loop
i=0
while(i<=len(s)):
    w=s[i] + w
print(w)