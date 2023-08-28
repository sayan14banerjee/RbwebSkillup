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

number = int(input("Enter the number: "))
if (is_magic_number(number)): # call the function 
    print("{} is a magic number".format(number))
else:
    print("{} isn't a magic number.".format(number))