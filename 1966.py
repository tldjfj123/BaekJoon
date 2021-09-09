from collections import deque

num = int(input())

def printer(n) :
    for _ in range(n) :
        i, idx = map(int, input().split())
        table = deque(list(map(int, input().split())))
        pointer = deque([False] * i)
        pointer[idx] = True
        count = 0
        while 1 :
            if table[0] == max(table) :
                count += 1
                if pointer[0] == True :
                    print(count)
                    break
                table.popleft()
                pointer.popleft()
            else :
                table.append(table.popleft())
                pointer.append(pointer.popleft())

printer(num)