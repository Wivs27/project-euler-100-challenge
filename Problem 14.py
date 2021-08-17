def findChainLength(n):
    count = 0
    while(n!=1):
        if n%2==0:
            count+=1
            n=n/2
        else:
            count+=1
            n=(3*n)+1
    return count+1

largestChain = 0
for i in range(1,1000000):
    chainLength = findChainLength(i)
    if chainLength > largestChain:
        largestChain = chainLength
        print(i)

