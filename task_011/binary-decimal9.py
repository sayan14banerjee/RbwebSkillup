class BinaryToDecimal:
    def convert(self, num):
        pow = int(len(num) - 1)
        sum = 0
        for i in num:
            sum += int(i) * 2 ** pow # it calculate the decimal

            pow -=1
        return sum

class Operation:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def sum(self):
        return self.num1 + self.num2

    def sub(self):
        return self.num1 - self.num2

    def mul(self):
        return self.num1 * self.num2

    def div(self):
        return self.num1 / self.num2

    def square(self):
        print(f"num 1 square { self.num1 ** 2} and num2 square {self.num2 ** 2}")


if __name__ == "__main__":
    try:
        num1 = (input("Enter number in binary "))
        num2 = (input("Enter number in binary "))
        for i in num1 :
            if i not in {'0', '1'}:  # check the input is binary or not
                raise ValueError()
            else:
                ans = BinaryToDecimal()
                n1 = ans.convert(num1)
        for i in num2:
            if i not in {'0', '1'}:  # check the input is binary or not
                raise ValueError()
            else:
                ans = BinaryToDecimal()
                n2 = ans.convert(num2)
        
        print(n1 ,'\n', n2)
        op = Operation(n1, n2)
        print(f"sum = {op.sum()}")
        print(f"sub = {op.sub()}")
        print(f"mul = {op.mul()}")
        print(f"div = {op.div()}")
        op.square()
    except ValueError:
        print('Enter only 1 or 0')

   