import math



for i in range(29,100000000):
    triNum = sum(range(1, i+1))
    count = 0
    for j in range(1,math.ceil(math.sqrt(triNum))):
        if triNum%j == 0:
            if j*j == triNum:
                count+=1
            else:
                count+=2
    if count > 500:
        print(triNum)




