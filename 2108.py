import sys
from collections import Counter

num = int(sys.stdin.readline())

def statistics(n) :
    table = []
    for _ in range(n) :
        table.append(int(sys.stdin.readline()))

    # 산술평균
    print(round(sum(table) / len(table)))

    # 중앙값
    table.sort()
    print(table[n // 2])

    # 최빈값
    check = list(set(table))
    if check == table :
        if len(table) == 1 :
            print(table[0])
        else :
            print(table[1])
    else :
        cnt = Counter(table).most_common(2)
        if cnt[0][1] > cnt[1][1] :
            print(cnt[0][0])
        else :
            print(cnt[1][0])
    # 범위
    print(max(table) - min(table))


statistics(num)