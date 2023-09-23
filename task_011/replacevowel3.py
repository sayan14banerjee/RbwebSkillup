class Solution:
    def vowel(self, str1):
        l =[] # list to store the char of the string
        for x in str1:
            if x in 'aeiouAEIOU': # check for vowel
                l.append('@') # replace vowel
            else:
                l.append(x)
        str2 = ''.join(l) # convert the list to string using join
        return str2

if __name__ == "__main__":
    # user input for value of two string
    str1 = input("Enter string: ")
    ans = Solution() # create new object
    print(f"The final string is: {ans.vowel(str1)}") # call the vowel function