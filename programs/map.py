

#map function is used to map a function to each element of iterable, it gives the output containing the same no. of elements as input
def square(x):
    return x*x

nums=[ i*2 for i in range(1,5)]

out = map(square,nums)
lambda_out= map(lambda x:x**2,nums)
print(list(out))
print(list(lambda_out))