a = 10
b = 30

# 1st method
temp = a  # 10
a = b
b = temp
print("Value of a after swap=", a)
print("Value of b after swap=", b)

# 2nd method
x = 5
y = 8
x = x + y
y = x - y
x = x - y
print(x)
print(y)

# 3rd method
p = 11
q = 54
q, p = p, q
print(p)
print(q)
