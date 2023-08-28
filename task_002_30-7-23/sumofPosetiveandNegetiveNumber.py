l=[12,-89,645,-5654,-465,545]
p_add=0 #to store the sum of postive number
n_add =0#to store the sum of negetive number
for i in l:
    if i>= 0:
        p_add = p_add + i #sum all p number
    else:
        n_add=n_add+i # add only negetive number
print(f"The sum of all posetive number is {p_add}")
print(f"The sum of all negetive number is {n_add}")