import sys

num = int(sys.stdin.readline())

def narak(num) :
    res = 0
    arr = [num]
    arr = list(map(int, input().split()))
    dem = max(arr)
    for i in range(len(arr)) :
        res += ((arr[i] / dem) * 100)
    print(res / num)
    return res / num


narak(num)