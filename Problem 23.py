
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

abundantNums = []
nonAbundantSums = [x for x in range(28123)]

abundantNums.append(12)
for i in range(13,28123):
    if sumOfDivisors(i) > i:
        abundantNums.append(i)

for i in range(0,len(abundantNums)):
    for j in range(i,len(abundantNums)):
        if abundantNums[i] + abundantNums[j] < 28123:
            nonAbundantSums[(abundantNums[i] + abundantNums[j])] = 0
        else:
            break

print(sum(nonAbundantSums))