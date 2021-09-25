num = int(input())

def large(n) :
    for _ in range(n) :
        arr = list(map(int, input().split()))
        arr.sort(reverse=True)
        print(arr[2])

large(num)