import sys

num = int(sys.stdin.readline())

def binary(number) :
    tmp = [int(input()) for _ in range(number)]
    res = []

    for i in range(number) :
        n = tmp[i]
        arr = []
        check = 0
        while n != 1 :
            if n % 2 == 1 :
                arr.append(str(1))
                check += 1
            else :
                arr.append(str(0))
            n = n // 2
        arr.append('1')
        
        result = list(filter(lambda x : arr[x] == '1', range(len(arr))))
        for r in result :
            res.append(str(r))
    print(' '.join(res))

binary(num)

