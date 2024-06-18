from itertools import permutations

def perm(arr):
    def gen_com(start, path):
        result.append(path)
        for i in range(start , len(arr)):
            gen_com(i+1, path+[arr[i]])
    result =[]
    gen_com(0,[] )
    return result

print(perm([1,2,3]))


def permute(arr):
    def _permute(current, remaining):
        if not remaining:
            result.append(current)
        else:
            for i in range(len(remaining)):
                _current= current + [remaining[i]]
                _rem=remaining[:i] + remaining[i+1:]
                _permute(_current, _rem)

    result = []
    _permute([], arr)
    return result

# Example usage
arr = [1, 2, 3]
print(permute(arr))


