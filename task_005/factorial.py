def fact(n):
    fact=1
    for i in range(1, n+1):
        fact=fact*i
    return fact

l=[1,2,3,4,5,6,7,8,9]

fact=list(map(lambda x: fact(x), l))

print(fact)