def primeFactorisation(n):
    p = 2
    while(n >= (p*p)):
        if(n % p == 0):
            print(p,"* ", end="")
            n = n/p
        else:
            p+=1
    print(n)


primeFactorisation(600851475143)