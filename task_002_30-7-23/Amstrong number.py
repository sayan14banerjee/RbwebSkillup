for i in range (1, 1001):
    s=i
    sum=0
    p=len(str(i))
    while i != 0:
        r = i % 10
        sum = sum+(r**p)
        i = i//10
    if s==sum:
        print(s,"is an Armstrong number")
