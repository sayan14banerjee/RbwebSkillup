# initialize two list
l1 = []
l2 = []
n=int(input("Enter the size of list: "))
#  input from user
for i in range (n):
    ele =int(input("Enter the element: "))
    # put it to l1 list
    l1.append(ele)
    # check for even
    if ele % 2 ==0:
        # put only even number in l2
        l2.append(ele)
print("The main list is ", l1)
print("The even list is ", l2)