#n=5

n=int(input("enter a number: "))
x = 1
while n != 0:

    for i in range(1, n+1):
        x =x*i

    print(x)
    break
