from array import array
import csv

total = 0
names = []
with open('Problem 22 Names.csv') as csvfile:
    reader = csv.reader(csvfile)
    names = list(reader)

names[0].sort()
for i in range(0, len(names[0])):
    wordScore = 0
    for j in names[0][i]:
        wordScore += (ord(j) - 64) 
    total += (wordScore * (i+1))

print(total)