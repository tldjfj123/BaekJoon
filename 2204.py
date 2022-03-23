import sys

def solution() :
    while 1 :
        n = int(sys.stdin.readline())
        
        if n == 0 :
            break
        else :
            arr = []
            for _ in range(n) :
                tmp = sys.stdin.readline().rstrip()
                arr.append((tmp, tmp.lower()))
            arr.sort(key = lambda x : x[1])

            print(arr[0][0])
        
solution()