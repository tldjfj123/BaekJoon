import sys

def binary() :
    arr = list(map(int, list(sys.stdin.readline().rstrip())))
    arr.reverse()


    res = []
    for i in range(0, len(arr), 3) :
        n = 0
        if i+3 < len(arr) :
            tmp = arr[i:i+3]
            for i in range(len(tmp)) :
                 n += (tmp[i] * (2 ** i))
            res.append(n)
        else :
            tmp = arr[i:]
            for i in range(len(tmp)) :
                 n += (tmp[i] * (2 ** i))
            res.append(n)
    res.reverse()
    print(''.join(list(map(str, res))))
   
binary()