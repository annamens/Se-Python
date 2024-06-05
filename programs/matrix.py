

rows = int(input('enter no. of rows:'))
cols = int(input('enter no. of cols:'))
lst=[]
for i in range(rows):
    a=[]
    for j in range(cols):
        a.append(int(input()))
    lst.append(a)
    print(lst)


for i in range(rows):
    for j in range(cols):
        print(lst[i][j], end=' ')
    print()

