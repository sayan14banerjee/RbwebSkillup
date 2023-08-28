l = [100, 20, 4, 455, 99]
#initialize max and seciond max
max = max(l[0], l[1])
secondmax = min(l[0], l[1])
#check second max
n = len(l)
for i in  l:
	if i > max:
		secondmax = max
		max = i
	elif i > secondmax and 	max != i:
		secondmax = i
	elif max == secondmax and secondmax != i:
		secondmax = i

print("Second highest number is : ",secondmax)
