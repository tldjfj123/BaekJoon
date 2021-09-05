import sys

num = int(input())

#sys.stdin.readline() >> input()보다 속도 빠름

for i in range(num) :
    a, b = sys.stdin.readline().split()
    a = int(a)
    b = int(b)
    print(a + b)