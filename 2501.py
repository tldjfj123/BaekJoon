a, b = map(int, input().split())

def factor(a, b) :
    arr = []
    for i in range(1, a+1) :
        if a % i == 0 :
            arr.append(i)
    try :
        print(arr[b-1])
    except :
        print(0)

factor(a, b)