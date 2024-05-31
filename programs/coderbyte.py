

def intersperse(str1,str2):
    min_len = min(len(str1),len(str2))
    result=[]
    for i in range(min_len):
        result.append(str1[i])
        result.append(str2[i])
    result.extend(str1[min_len:])
    result.extend(str2[min_len:])
    return ''.join(result)

print(intersperse("prettykotte",'shree'))

def search(strArr):
    result={}
    for item in strArr:
        for data in item.split():
            key, value = data.split(':')
            value=int(value)
            if key in result:
                result[key] += value
            else:
                result[key] = value
    if result[key]==0:
        del result[key]

    print(' '.join(f"{key}:{result[key]}" for key in result))
search(['A:3','B:4','A:-9'])

