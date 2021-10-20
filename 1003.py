def fib_calc(num) :
    arr = []
    for i in range(0, num+1) :
        if i == 0 :
            arr.append((1, 0))
        elif i == 1 :
            arr.append((0, 1))
        else :
            a = arr[i-2][0] + arr[i-1][0]
            b = arr[i-2][1] + arr[i-1][1]
            arr.append((a, b))
    return arr[-1]

def main() :
    n = int(input())
    for _ in range(n) :
        num = int(input())
        print("{} {}".format(fib_calc(num)[0], fib_calc(num)[1]))

main()