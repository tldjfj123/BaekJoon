# 선입선출!!

class queue :
    def __init__(self) :
        self.items = []
    
    def empty(self) :
        if len(self.items) == 0 :
            return 1
        return 0
    
    def enqueue(self, val) :
        self.items.append(val)
    
    def dequeue(self) :
        if len(self.items) == 0 :
            return -1
        return self.items.pop(0)
    
    def size(self) :
        return len(self.items)
    
    def front(self) :
        if len(self.items) == 0 :
            return -1
        return self.items[0]
    
    def back(self) :
        if len(self.items) == 0 :
            return -1
        return self.items[-1]

import sys

q = queue()

num = int(sys.stdin.readline())

def function(n) :
    for _ in range(n) :
        f = sys.stdin.readline().rstrip()
        if f == 'pop' :
            print(q.dequeue())
        elif f == 'size' :
            print(q.size())
        elif f == 'empty' :
            print(q.empty())
        elif f == 'front' :
            print(q.front())
        elif f == 'back' :
            print(q.back())
        else :
            tmp1, tmp2 = f.split()
            q.enqueue(int(tmp2))

function(num)