import heapq
import sys

def solution() :
    t = int(sys.stdin.readline())
    
    for _ in range(t) :
        k = int(sys.stdin.readline())
        max_heap = []
        min_heap = []
        check = [False] * k
        
        for i in range(k) :
            o, n = sys.stdin.readline().split()
            
            if o == 'I' :
                heapq.heappush(min_heap, (int(n), i))
                heapq.heappush(max_heap, (-int(n), i))
                check[i] = True
            elif n == '-1' :
                if n == '-1' :
                    while min_heap and not check[min_heap[0][1]] :
                        heapq.heappop(min_heap)
                    if min_heap :
                        check[min_heap[0][1]] = False
                        heapq.heappop(min_heap)
            else :
                while max_heap and not check[max_heap[0][1]] :
                    heapq.heappop(max_heap)
                if max_heap :
                    check[max_heap[0][1]] = False
                    heapq.heappop(max_heap)
    
        while min_heap and not check[min_heap[0][1]] :
            heapq.heappop(min_heap)
        while max_heap and not check[max_heap[0][1]] :
            heapq.heappop(max_heap)
        
        if max_heap and min_heap :
            print(f'{-max_heap[0][0]} {min_heap[0][0]}')
        else :
            print('EMPTY')

solution()