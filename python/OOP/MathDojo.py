class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        self.result += num
        for numbers in nums:
            self.result += numbers
        return self
    def subtract(self, num, *nums):
        self.result -= num
        for numbers in nums:
            self.result -= numbers
        return self
# create an instance:
md = MathDojo()
# to test:
x = md.add(2).add(2,5,1).add(2,5,1,8).subtract(3,2).subtract(1).subtract(1,1,1,1).result
print(x)	# should print 5
# run each of the methods a few more times and check the result!
