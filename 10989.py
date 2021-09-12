import sys

num = int(sys.stdin.readline())

def sorting(n) :
    check = [0] * 10000
    for _ in range(n) :
        i = int(sys.stdin.readline())
        check[i-1] += 1
    
    for i in range(len(check)) :
        if check[i] > 0 :
            for _ in range(check[i]) :
                print(i+1)


sorting(num)