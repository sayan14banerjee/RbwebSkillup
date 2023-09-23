class Solution:
    def count(self, str1):
        count1 = 0 # count for vowel
        count2 = 0 # count for consonants
        for i in str1:
            if i in "aeiouAEIOU": # check for vowels
                count1 += 1
            else:
                count2 += 1
        # give the counts
        print(f'''number of vowel is: {count1}
number of consonants is {count2} ''')


if __name__ == "__main__":
    str1 = input("Enter string: ") # user input for value
    ans = Solution() # create new object
    ans.count(str1) # call the count function