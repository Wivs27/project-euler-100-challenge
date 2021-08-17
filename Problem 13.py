f = open('Problem 13 Number.txt','r')
numbers = []
for line in f.readlines():
    numbers.append(line.strip('\n'))
f.close()

sum = 0
for i in range(0,100):
    sum += int(numbers[i])

print(str(sum)[:10])