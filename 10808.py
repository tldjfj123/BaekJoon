from collections import Counter

def solution() :
    s = input()

    table = [chr(i) for i in range(97, 123)]
    tmp = Counter(s)

    print(' '.join(list(map(str, [tmp[table[i]] for i in range(len(table))]))))

solution()