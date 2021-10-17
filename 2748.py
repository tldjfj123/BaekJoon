def fib() :
    arr = []
    num = int(input())
    for i in range(num) :
        if i < 2 :
            arr.append(1)
        else :
            arr.append(arr[i-2] + arr[i-1])
    print(arr[num-1])

fib()