import pprint
a = {'name':'srinivas', "id":1116, 'address':'hyd'}
b= {'car':True, 'home':False}
print(a)
#merge using bit wise operator
merge= a|b
print(merge)
x={'name':'srinivas', "id":1116, 'address':'hyd'}
y= {'car':True, 'home':False}
#merge using update
y.update(x)
print(y)
pprint.pprint(y)
l={'name':'srinivas', "id":1116, 'address':'hyd'}
m= {'car':True, 'home':False}
print({**l, **m})

data = {'name': 'John', 'age': 30, 'languages': ['Python', 'JavaScript', 'Java']}
pprint.pprint(data)
