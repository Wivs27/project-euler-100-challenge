import math

fact = math.factorial(100)
sum = 0
while fact != 0:
    sum += fact % 10
    fact = fact // 10

print(sum)