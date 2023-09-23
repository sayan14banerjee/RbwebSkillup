class Solution:
    def compare(self, str1, str2):
        count1 = 0  # count for string 1
        count2 = 0 # count for string 2
        for i in str1: # count the char in string 1
            count1 += 1
        for j in str2: # count the char in string 2
            count2 += 1
        # compare the number of chr of each string return the greater
        if count1 > count2:
            return str1
        elif count1 < count2:
            return str2
        else:
            return "Both are equal!"

if __name__ == "__main__":
    # user input for value of two string
    str1 = input("Enter string 1 ")
    str2 = input("Enter string 2 ")
    ans = Solution() # create new object
    print(f"{ans.compare(str1, str2)} is longer") # call the compare function