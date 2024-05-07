#iterator
#an object used to iterate over iterable objects like list tuple, sets
#uses iter() and next(), it gives a iterator object

string =[1,2,3]
iter=iter(string)
print(type(iter))
print(next(iter))
print(next(iter))
print("=======")
#advance way
n=[1,2,3,4]
for i in n:
    print(i)

#generator
# a function with yield keyword instead of return becomes a generator
# it gives  a generator object
def gen_fun():
    yield "hello!"
    yield "Python"
    yield "world."
obj =gen_fun()
print(type(obj))
print(next(obj))
print(next(obj))

for value in gen_fun():
    print(value)