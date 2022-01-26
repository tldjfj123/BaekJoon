import sys

def dna() :
    n, m = map(int, sys.stdin.readline().split())
    board = [sys.stdin.readline().rstrip() for _ in range(n)]
    res = []
    count = []
    
    for i in range(m) :
        tmp = dict()
        for j in range(n) :
            if board[j][i] not in tmp.keys() :
                tmp[board[j][i]] = 1
            else :
                tmp[board[j][i]] += 1
        tmp = list(tmp.items())
        tmp.sort(key = lambda x : (-x[1], x[0]))
        res.append(tmp[0][0])
        if len(tmp) != 1 :
            for i in range(1, len(tmp)) :
                count.append(tmp[i][1])
    print(''.join(res))
    print(sum(count))

dna()