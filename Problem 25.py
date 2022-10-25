
a = True
f1 = 1
f2 = 1
term = 2
while a:
   temp = f1 + f2
   f1 = f2
   f2 = temp
   term += 1
   if len(str(f2)) >= 1000 :
       a = False
       print(term) 
