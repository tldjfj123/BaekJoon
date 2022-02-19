import sys

def solution() :
    t = int(sys.stdin.readline())

    for _ in range(t) :
        a, b = sys.stdin.readline().split()
        if sorted(list(a)) == sorted(list(b)) :
            print(f"{a} & {b} are anagrams.")
        else :
            print(f"{a} & {b} are NOT anagrams.")            
solution()