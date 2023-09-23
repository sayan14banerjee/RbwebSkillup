class Solution:
    def reverse(self, str):
        str1 = '' # string to store reverse
        for i in str:
            str1 = i + str1 # every char of string store reversely in the second string
        return str1


if __name__ == "__main__":
    str = input('Enter string: ') # user input
    ans = Solution() # create new object
    print(f"the reverse string is: {ans.reverse(str)}") # call the reverse function
