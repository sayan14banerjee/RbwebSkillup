n = int(input())
sum = 0
while(n > 0):
    r = n % 10
    n = n//10
    sum = sum + r
print(sum)