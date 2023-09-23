class Solution:
    def reprint(self, str):
        l = [str[0], str[-1]]
        str2 = ''.join(l)
        return int(str2)


if __name__ == "__main__":
    str = input("Enter only numbers") # user input for value
    if not str.isalpha(): # check for integers values
        ans = Solution() # create new object
        print(ans.reprint(str)) # call the function
    else:
        raise ValueError("Enter integers value only....") # create error