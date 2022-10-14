def sumOfDivisors(n):
    sum = 1
    if n % 2 != 0:
        for i in range(3,n,2):
            if n % i == 0:
                sum += i
    else:
        for i in range(2,n):
            if n % i == 0:
                sum += i
    return sum

amicableNumbers = []
alreadyChecked = False

for i in range(2, 10000):
    alreadyChecked = False
    for x in amicableNumbers:
        if x == i:
            alreadyChecked = True
            break
    if alreadyChecked:
        continue
    pairToCheck = sumOfDivisors(i)
    if pairToCheck == i:
        continue
    if sumOfDivisors(pairToCheck) == i:
        amicableNumbers.append(i)
        amicableNumbers.append(pairToCheck)

finalAnswer = 0
for x in amicableNumbers:
    finalAnswer += x

print(finalAnswer)
