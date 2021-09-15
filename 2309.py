from itertools import combinations

def short() :
    height = []
    for _ in range(9) :
        height.append(int(input()))
    table = list(combinations(height, 7))

    for t in table :
        if sum(t) == 100 :
            t = list(t)
            t.sort()
            for tt in t :
                print(tt)
            break

short()