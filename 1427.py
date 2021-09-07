import sys

s = sys.stdin.readline().rstrip()

sol = list(map(int, s))

sol.sort(reverse=True)

stoi = [str(i) for i in sol]

print(''.join(stoi))