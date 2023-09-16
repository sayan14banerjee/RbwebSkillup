# Read a float:
# b = float(input())
# Print a value:
# print(a, b)
a = int(input())
b = int(input())
c = int(input())
if a % 2 ==0:
    desk1 = a//2
else :
    desk1 = a//2 +1
if b % 2 ==0:
    desk2 = b//2
else :
    desk2 = b//2 +1
if c % 2 ==0:
    desk3 = c//2
else :
    desk3 = c//2 +1

desk = desk1 + desk2 + desk3
print(desk)