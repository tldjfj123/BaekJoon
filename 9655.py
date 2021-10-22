import sys

def stone() :
    n = int(sys.stdin.readline())
    if n % 2 == 1 :
        print("SK")
    else :
        print("CY")

stone()