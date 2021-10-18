import sys

def ppap() :
    num = int(sys.stdin.readline())
    s = sys.stdin.readline().rstrip()
    count = 0
    idx = 0
    for _ in range(num-3) :
        if s[idx:idx+4] == "pPAp" :
            count += 1
            idx += 4
        else :
            idx += 1
    print(count)

ppap()