lst = ['sri', 1, 4, 6, 1, 4, 5, 8, 'sri']
indices ={}
for i, item in enumerate(lst):
    if item in indices:
        indices[item].append(i)
    else:
        indices[item] =[i]
for item, index in indices.items():
    if len(index) >1:
        print(f'duplicate of {item} occurs at {index}')