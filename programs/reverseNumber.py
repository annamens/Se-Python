n =359578
rev=0

while n != 0:
    x =n%10
    rev = rev*10+x
    n= n//10
print(rev)

lst = [[1,2],[3,4,[6,7],5]]

res=[item for sublst in lst for item in sublst]
print(res)

ss=[]
for i in lst:
    ss.extend(i)
print(ss)