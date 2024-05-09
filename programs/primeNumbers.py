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
b=20
while a<=b:
    c = True
    for i in range(2, int(a/2)+1):
        if a%i==0:
            c = False
            break
    if c:
        print(a,end=" ")
    a=a+1
#print first n prime numbers
def is_prime(num):
    if num<=1:
        return False
    for i in range(2,num//2+1):
        if num%i==0:
            return False
    return True
def print_primes(n):
    primes=[]
    num=2
    while len(primes)<n:
        if is_prime(num):
            primes.append(num)
        num+=1
    print(primes)
print_primes(9)