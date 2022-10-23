daysInMonths = [31,28,31,30,31,30,31,31,30,31,30,31]
currentDay = 1
total = 0 

for i in range(1901,2001):
    if i % 4 == 0:
        daysInMonths[1] = 29
    else:
        daysInMonths[1] = 28
    for j in range(0,12):
        currentDay = ((currentDay + (daysInMonths[j] % 7)) % 7)
        if currentDay == 6:
            total += 1
        
print(total)