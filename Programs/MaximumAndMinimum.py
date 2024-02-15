n =[134,23,52,89,45,71,69,17,2]
max=n[0]
for i in range(0,len(n)):
    if n[i] > max  :
        max =n[i]

print(max)

min =n[0]
for i in range(0,len(n)):
    if n[i] < min:
        min = n[i]
print(min)
