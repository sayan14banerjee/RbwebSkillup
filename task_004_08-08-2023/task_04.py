def sum_of_all_number(l):
    sum = 0 # initialize sum variable to 0
    for i in l:
        sum = sum + i
    return sum

def list_of_even(l1):
    l2 = []
    for i in l1:
        # check for even
        if i % 2 ==0:
            # put only even number in l2
            l2.append(i)
    return l2

def reverse_list(l1):
    l2=[] # reverse list
    for i in l:
        l2.insert(0, i) # insert every element of the l list in 0 position
    return l2

def largest_ele(l):
    max=l[1] # assume the first element is maximum
    for i in l :
        if i>max:
            max=i
    return max

def unique_ele(l):
    l2= [] # list to store unique value
    for i in l:
        if i not in l2: # check for duplicate
            l2.append(i)
    return l2

def cumulative (l1):
    l2 = [] # list to store the cumulative sum
    sum = 0 # to sum the elements
    for i in l:
        sum +=i
        l2.append(sum) # store the sum of previous elements
    return l2

def intersection():
    l1 = [12, 321, 32, 469, 987, 65]
    l2 = [12, 54, 321, 987, 5465, 321]
    l3=[] # intersection list
    #chek the long list for keep duplicates
    if len(l1) > len(l2):
        for i in l1:
            if i in l2: # check for common
                l3.append(i)
    else:
        for i in l2:
            if i in l1: # check for common
                l3.append(i)
    return l3

def rotate(l):
    n = int(input("Enter the rotate point: "))
    l2 = l[n:] + l[:n] # add the last par of list before the first of the list
    return l2

def sort_by_age():
    l = [("Sayan", 12), ("Shyam", 29), ("Rahul", 22), ("Asif", 25)]
    # bubllee sort
    for i in range(len(l)):
        for j in range(len(l)-i-1):
            if l[j][1] > l[j+1][1]: #compare only age 
                l[j], l[j+1] = l[j+1], l[j] #change every item of list 
    return l

def max_diff(l):
    max=l[0]
    min=l[0]
    for i in l:
        if max<i : #check the max element
            max = i
        if min>i and l.index(max) > l.index(min) : # check the min element which is before the max element
            min = i
    return max-min

def substring():
    l = ["sayan", "is", 'good', 'boy']
    sub = "y" # this is the specific substring
    new = [] # new list to store the specific string
    for i in l:
        if sub in i: # check for substring
            new.append(i)
    return new

def decimal_binary_conversion():
    choise = input("Which conversion you want \n press b for binary to decimal \n press d for decimal to binary ")
    if choise == 'b': # bnary to decimal 
        n = (input("Enter the number in binary : "))
        pow = int(len(n) - 1)
        sum = 0
        for i in n:
            if i not in {'0', '1'}: # check the input is binary or not
                print('Enter only 1 or 0')
                return 
            else:
                sum += int(i) * 2 ** pow # it calculate the decimal

            pow -=1
        return sum
    elif choise == 'd': # dcimal to binary
        n = int(input("Enter the number in decimal: "))
        l=[]
        while(n > 0):
            r = n % 2
            n = n // 2
            l.insert(0, r) #add the binary number in list 
        return l
    else: 
        return("ENter only b or d")
def is_magic_number(number):
    sum = 0 
    while(number > 0 or sum > 9): # loop until the thee sum of the digit become single digit 
        if number == 0: # if the n becom 0 but the sum is not single digit 
            number = sum # sum become number and continue the sumation 
            sum = 0
        digit= number %10 # take last digit 
        number  //= 10 # remove the last digit 
        sum += digit # sum the digit 
    if sum == 1: # check for magic number 
        return True
    else:
        return False

l=[12,65,4,54,54,65,3]
#take question no and give the ans    
c=True
# unlimited time give ans
while(c):
    qno=int(input("Enter the question no: "))
    if qno > 0 and qno < 14: #check for question number 
        if qno == 1: 
             print(l)
             print(sum_of_all_number (l))
        elif qno == 2:
            print(l)
            print(list_of_even(l))
        elif qno == 3:
            print(l)
            print(reverse_list(l))
        elif qno == 4:
            print(l)
            print(largest_ele(l))
        elif qno == 5:
            print(l)
            print(unique_ele(l))
        elif qno == 6:
            print(l)
            print(cumulative(l))
        elif qno == 7:
            print(l)
            print(intersection())
        elif qno == 8:
            print(l)
            print(rotate(l))
        elif qno == 9:
            print(sort_by_age())
        elif qno == 10:
            print(l)
            print(max_diff(l))
        elif qno == 11:
            print(substring())
        elif qno == 12 :
            print(decimal_binary_conversion())
        elif qno == 13:
            number = int(input("Enter the number: "))
            if (is_magic_number(number)): # call the function 
                print("{} is a magic number".format(number))
            else:
                print("{} isn't a magic number.".format(number))
        else:
            print("Error" )
    else:
        print("Please enter valuse 1-13")
    # take choise to continue or exit 
    choise=input("Enter y to continue or press any key exit")
    c=(choise=='y')
