a, b = map(int, input().split())

def number(a, b) :
    arr = []
    count = 0
    while len(arr) <= b :
        count += 1
        for _ in range(count) :
            arr.append(count)
    print(sum(arr[a-1 : b]))

number(a, b)