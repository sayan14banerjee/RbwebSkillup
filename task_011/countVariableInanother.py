class Solution:
    def count(self, var1, var2):
        count = 0
        for x in var1: # visit every char in var1
            if x == var2: # compare every char of var1 withe var2
                count += 1 # if equal count 1
        return count
if __name__ == "__main__":
    # user input for value of two string
    var1 = input("Enter the string: ")
    var2 = input("Enter a single digit char: ")
    if len(var2) == 1:
        ans = Solution() # create new object
        print(f"The number of {var2} is {ans.count(var1, var2)}") # call the compare function
    else :
        raise ValueError("Enter only single digit char")