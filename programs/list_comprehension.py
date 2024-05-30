import pprint
#list comprehension
list_ = [i*4 for i in range(1,5)]
print(list_)

pprint.pprint(list_)


#tuple comprehension
a=(4,5,6)
print(a)
tup = ((i+5) for i in range(1,7))
print(tup)
for _ in tup:
    print(_, end=' ')
