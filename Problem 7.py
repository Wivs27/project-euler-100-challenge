def Sieve(n):
    prime = [True for i in range(n+1)]
    p = 2
    while(p*p <= n):
        if(prime[p] == True):
            for i in range(p*p,n+1,p):
                prime[i] = False
        p += 1

    numOfPrimes = 0
    for p in range(2, n+1):
        if prime[p]:
            numOfPrimes += 1
            if numOfPrimes == 10001:
                print(p)


n = 1000000
Sieve(n)