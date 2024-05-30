str = ["srinivas", "new", "old", "chocolate"]
rev = []
for i in range(len(str) - 1, -1, -1):
    rev.append(str[i])
print(rev)

print(sorted(str,reverse=True))