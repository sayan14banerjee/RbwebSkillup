n=input("Enter a string: ")
#empty string
w = ""
#add the charecters of the n in w but reversly
for i in n:
    w = i + w #Concatenate 
#check palindrome 
if w==n:
    print("{} is palindrome".format(n))
else:
    print("{} is not palindrome".format(n))