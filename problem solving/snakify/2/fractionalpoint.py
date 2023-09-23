n = float(input())
x = str(n)
x1 = x.split('.')
c = x1[-1]
c1= int(c) / 10 ** len(c)
print(c1)