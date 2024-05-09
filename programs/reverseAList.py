lst = [10, 11, 12, 13, 14, 15]
rev = []
print("Before reverse: ", lst)
# print(len(lst))

for i in range(len(lst) - 1, -1,-1):
    rev.append(lst[i])

print("After reverse: ",rev)
