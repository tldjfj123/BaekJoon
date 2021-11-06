from collections import deque
import sys

def trip() :
    t = int(input())

    for _ in range(t) :
        n, m = map(int, sys.stdin.readline().split())
        graph = [[] for _ in range(n+1)]

        for i in range(m) :
            d, a = map(int, sys.stdin.readline().split())
            graph[d].append(a)
            graph[a].append(d)
        
        visited = [False] * (n+1)

        queue = deque([1])
        visited[1] = True

        while queue :
            v = queue.popleft()
            for i in graph[v] :
                if not visited[i] :
                    queue.append(i)
                    visited[i] = True
        
        print(sum(visited)-1)

trip()