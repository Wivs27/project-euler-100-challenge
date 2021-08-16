def pythagoreanTripletCheck(a,b,c):
    if a<b and b<c and (pow(a,2)+pow(b,2)==pow(c,2)):
        return True
    else:
        return False

for a in range(0,332):
    for b in range(2,500):
        for c in range(3,997):
            if(a+b+c==1000):
                if(pythagoreanTripletCheck(a,b,c)):
                    print(a,"*",b,"*",c,"=",a*b*c)

