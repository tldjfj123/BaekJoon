import heapq
import sys

def card() :
    n = int(sys.stdin.readline())
    heap = []
    
    res = 0
    for _ in range(n) :
        heapq.heappush(heap, int(sys.stdin.readline()))
    
    if len(heap) == 1 :
        return 0
    else :
        res = []
        while len(heap) != 1 :
            a = heapq.heappop(heap)
            b = heapq.heappop(heap)
            tmp = a + b
            res.append(tmp)
            heapq.heappush(heap, tmp)
        return sum(res)
    
print(card())