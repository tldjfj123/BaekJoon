from collections import deque

def virus() :
    n = int(input())
    c = int(input())
    graph = [[] for _ in range(n+1)]

    for _ in range(c) :
        node, connected = map(int, input().split())
        graph[node].append(connected)
        graph[connected].append(node)

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

virus()