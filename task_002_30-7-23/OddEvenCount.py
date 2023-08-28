l=[3,321,54,58,51,53,59,56,564,47]
#count for even
cEv=0
#count for odd
cOdd= 0
#check for eve or odd
for i in l:
    if(i%2==0):
        cEv+=1
    else:
        cOdd +=1
print(f" Total number of odd number is {cOdd} and\n Total number of eveenis {cEv} ")
