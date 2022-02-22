import sys
from collections import Counter

def solution() :
    n, m = map(int, sys.stdin.readline().split())
    words = []
    
    for _ in range(n) :
        tmp = sys.stdin.readline().rstrip()
        if len(tmp) >= m :
            words.append(tmp)
    res = Counter(words).most_common()
    res.sort(key = lambda x : (-x[1], -len(x[0]), x[0]))

    for r in res :
        print(r[0])
        
solution()