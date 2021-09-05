import sys

num = int(input())

for i in range(num) :
    a, b = sys.stdin.readline().split() 

    a = int(a)
    b = int(b)

    print('Case #{}: {}'.format(i+1, a + b))