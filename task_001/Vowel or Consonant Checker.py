# s=input("Enter a string(non Numarical): ")
# if s.isdigit():
#     print('invalid')
# else:
#     for i in s:
#         if i== "a" or i=="e" or i == "i" or i == "o" or i== "u":
#             print(i, "=vowel")
#         else:
#             print(i, "=consonant")
s=input("Enter a charecter: ")
if s.isdigit():
    print('invalid')
else:
    if len(s)<2 and len(s)>0:
        if s== "a" or s=="e" or s == "i" or s == "o" or s== "u":
            print(s, "=vowel")
        else:
            print(s, "=consonant")
    else:
        print('invalid')