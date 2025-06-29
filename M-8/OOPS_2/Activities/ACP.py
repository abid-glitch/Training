class SumOfThree:

    def __init__(self, a, b, c):
        self.val1 = a
        self.val2 = b
        self.val3 = c

    def displaySum(self):
        total = self.val1 + self.val2 + self.val3
        print('Sum:', total)

a = int(input("Input first number: "))
b = int(input("Input second number: "))
c = int(input("Input third number: "))

obj = SumOfThree(a, b, c)
obj.displaySum()
