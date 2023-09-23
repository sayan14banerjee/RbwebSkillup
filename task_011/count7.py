class Solution:
    def count(self, str1):
        countalpha = 0 # count for alphabet
        countsymbol = 0 # count for symbol
        countnum =0 # count for numeric
        for i in str1:
            if i.isalpha(): # check for alphabet
                countalpha += 1
            elif i.isdigit(): # check for number
                countnum += 1
            else: # check for symbol
                countsymbol += 1
        print(f"""number of alphabet {countalpha}
    number of number {countnum}
    number of symbol {countsymbol}""")


if __name__ == "__main__":
    str = input("Enter value") # user input
    ans = Solution() # create new object
    ans.count(str) # call the count function