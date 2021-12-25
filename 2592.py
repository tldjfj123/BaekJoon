import sys
from collections import Counter

def represent() :
    arr = []
    
    for _ in range(10) :
        arr.append(int(sys.stdin.readline()))
    
    print(sum(arr) // len(arr))
    
    cnt = Counter(arr).most_common()
    print(cnt[0][0])    
    
represent()