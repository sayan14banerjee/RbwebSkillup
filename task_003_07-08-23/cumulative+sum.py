l=[10, 20, 30, 40, 50]
l2 = [] # list to store the cumulative sum
sum = 0 # to sum the elements
for i in l:
    sum +=i
    l2.append(sum) # store the sum of previous elements
print("The cumulative sum is ", l2)