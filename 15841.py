def fib(n) :
    arr = []
    for i in range(n) :
        if i < 2 :
            arr.append(1)   
        else :
            arr.append(arr[i-2] + arr[i-1])
    return arr[-1]

def virus() :
    while 1 :
        num = int(input())
        if num == -1 :
            break
        else :
            print("Hour {}: {} cow(s) affected".format(num, fib(num)))

virus()
