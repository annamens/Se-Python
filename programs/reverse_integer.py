#method-1
n = 1234
rev =0
while n>0:
    x = n%10
    rev = rev*10+x
    n =n//10
print(rev)

#method-2
m=4567
rev_int = int(str(m)[::-1])
print(rev_int)