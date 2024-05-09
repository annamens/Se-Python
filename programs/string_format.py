a=5
b=9
print(f'values are: {a,b}')
#*y is called packing
x,*y = 1, 3, 4
print(x, y)

name ='python'
no =5

#old style technique
format1= "%s is a language with no: %d"%(name,no)
#new style
format2= "{} is a language with no: {}".format(name, no)
#f-string  python 3.6 +
format3= f'{name} is a language with no: {no}'

print(format1)
print(format2)
print(format3)

