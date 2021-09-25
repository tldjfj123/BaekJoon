def train() :
    res = []
    count = 0
    for _ in range(10) :
        o, i = map(int, input().split())
        count -= o
        count += i
        res.append(count)
    print(max(res))

train()