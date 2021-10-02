from itertools import combinations
num = int(input())

def stick(n) :
    arr = [1, 2, 4, 8, 16, 32,64]
    for i in range(1, len(arr)+1) :
        result = list(combinations(arr, i))
        for r in result :
            if n == sum(r) :
                return len(r)

print(stick(num))