n=14

count =0
if n>0:
    for i in range(1,n+1):
        if n%i==0:
            count=count+1
    if count==2:
        print("Num is  prime")
    else:
        print("Num is not prime")

#print primes b/w range
a =5
b=97
while a<=b:
    c = True
    for i in range(2, a//2):
        if a%i==0:
            c = False
            break
    if c:
        print(a,end=" ")
    a=a+1
