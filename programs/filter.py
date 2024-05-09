

#filter is used to filter the items in a iterable, it gives output which is less than or equal to the input elements
nums=[i for i in range(1,9)] #list comprehension
def is_even(n):
    if n%2==0:
        return n

filtered= filter(is_even,nums)
lambda_filter = filter(lambda x: x%2!=0,nums)
print(type(filtered))
print(list(filtered))
print(list(lambda_filter))