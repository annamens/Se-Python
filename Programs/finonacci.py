#method-1
n=8
a=0
b=1
for i in range(0,n):
    print(a, end =" ")
    sum=a+b
    a,b=b, sum
    # b=sum
#method-2 recursive method
print()
def fibo(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fibo(n-1)+fibo(n-2)
print(fibo(4))
n=8
for i in range(n):
    print(fibo(i), end=' ')









