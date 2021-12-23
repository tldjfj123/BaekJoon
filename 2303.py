import sys
from itertools import combinations

def numbergame() :
    n = int(input())
    
    fin = [0]
    for _ in range(n) :
        card = list(map(int, sys.stdin.readline().split()))
        tmp = list(combinations(card, 3))
        res = list(map(lambda x : sum(x) % 10, tmp))
        fin.append(max(res))
        
    fin = list(filter(lambda x : fin[x] == max(fin), range(len(fin))))
    
    if len(fin) == 1 :
        print(sum(fin))
    else :
        print(max(fin))
                            
numbergame()