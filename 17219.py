import sys

def password() :
    n, m = map(int, sys.stdin.readline().split())
    sites = dict()

    for _ in range(n) :
        address, pw = sys.stdin.readline().rstrip().split()
        sites[address] = pw

    for _ in range(m) :
        want_to_find = sys.stdin.readline().rstrip()
        print(sites[want_to_find])

password()