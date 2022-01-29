import sys
from itertools import combinations

def lotto() :
    while 1 :
        n = list(sys.stdin.readline().split())
        
        if len(n) == 1 :
            break
        else :
            nums = n[1:]
            t = list(combinations(nums, 6))
            
            for i in t :
                print(' '.join(i))
            print()

lotto()