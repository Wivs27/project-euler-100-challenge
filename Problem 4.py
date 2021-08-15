def isPalindrome(n):
    temp=n
    rev=0
    while(n>0):
        dig=n%10
        rev=rev*10+dig
        n=n//10
    if(temp==rev):
        return True
    else:
        return False

biggestNumber = 9009
for i in range(100,1000):
    for x in range(100,1000):
        if(isPalindrome(x*i) and (x*i)>biggestNumber):
            biggestNumber=x*i
            print(biggestNumber,"by doing ",x,"*",i)