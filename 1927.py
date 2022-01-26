import heapq
import sys

def solution() :
    n = int(sys.stdin.readline())
    heap = []
    
    for _ in range(n) :
        t = int(sys.stdin.readline())
        if t == 0 :
            if len(heap) == 0 :
                print(0)
            else :
                print(heapq.heappop(heap))
        else :
            heapq.heappush(heap, t)

solution()