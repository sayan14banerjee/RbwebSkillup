n = int(input())
m = int(input())
t = m/n
t1 = m//n
if float(t1) != t:
    t1 +=1 
print(t1)