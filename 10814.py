import sys

num = int(sys.stdin.readline())

def new_sort(n) :
    table = []
    count = 0
    for _ in range(n) :
        age, name = sys.stdin.readline().split()
        table.append((age, name, count))
        count += 1

    table.sort(key = lambda x : (int(x[0]), int(count)))

    for t in table :
        print("{} {}".format(t[0], t[1]))
    
new_sort(num)