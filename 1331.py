from collections import deque

def knight() :
    # A ~ Z = 65 ~ 90
    visited = [input() for _ in range(36)]
    visited = deque([str(int(ord(visited[i][0])) - 64) + visited[i][1] for i in range(len(visited))])
    visited.appendleft(visited.pop())
    visited = list(visited)    

    if len(visited) != len(list(set(visited))) :
        return "Invalid"
    else :
        for i in range(len(visited)-1) :
            if abs(int(visited[i+1][0]) - int(visited[i][0])) > 2 or abs(int(visited[i+1][1]) - int(visited[i][1])) > 2 :
                return "Invalid"
            else :
                if abs(int(visited[i+1][0]) - int(visited[i][0])) == 2 and abs(int(visited[i+1][1]) - int(visited[i][1])) != 1 :
                    return "Invalid"
                if abs(int(visited[i+1][0]) - int(visited[i][0])) == 1 and abs(int(visited[i+1][1]) - int(visited[i][1])) != 2 :
                    return "Invalid"
        return "Valid"

print(knight())