import sys

def card() :
    n = int(sys.stdin.readline())
    table = dict()
    for _ in range(n) :
        i = int(sys.stdin.readline())
        if i in table.keys() :
            table[i] += 1
        else :
            table[i] = 1
            
    table = list(table.items())
    table.sort(key = lambda x : (-x[1], x[0]))
    
    print(table[0][0])    
    
card()