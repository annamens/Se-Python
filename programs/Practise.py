lst = [1, 2, 3, 4, 5, 3, 6, 7, 3]

import string

print(string.ascii_letters)
var = []
for i in range(0, len(lst) - 1):
    for j in range(i + 1, len(lst) - 1):
        if lst[i] == lst[j]:
            if lst[i] not in var:
                var.append(lst[i])
            else:
                print(i, ': ', lst[i])
