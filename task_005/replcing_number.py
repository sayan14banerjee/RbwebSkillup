result=list("FIZZBUZZ" if x%3==0 and x%5==0 else "Fizz" if x % 3 == 0 else "Buzz" if x % 5 == 0 else x for x in range(1, 101))
#multiples of 3 with "Fizz," multiples of 5 with "Buzz," and multiples of both 3 and 5 with "FizzBuzz"
print(result)