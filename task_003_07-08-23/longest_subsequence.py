def longest_subsequence(l):
    l.sort() #sort the list
    ls = [l[0]] #longest subsquence 
    cs = [l[0]] #curent subsequence

    for i in range(1, len(l)):
        if l[i] - l[i - 1] == 1: #if the ith value is the subsequence of the previous value 
            cs.append(l[i]) #sore it to curent sequence 
        else: # or it checks the logest is small tha currnt 
            if len(cs) > len(ls):
                ls = cs.copy() #then it copy current to longest 
            cs = [l[i]] #current will be curent element 

    if len(cs) > len(ls):
        ls = cs

    return ls

# Input: list of integers
l = [1,2,3,5,6,7,8,11,12]
print("Longest consecutive subsequence:",longest_subsequence(l))
