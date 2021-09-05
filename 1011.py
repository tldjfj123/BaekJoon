import sys
import math

num = int(input())

def astronaut(n) :
    for i in range(n) :
        s, f = map(int, sys.stdin.readline().split())
        d = f - s
        count = 0

        num = math.floor(math.sqrt(d))
        num_square = num ** 2
        increased_num = math.sqrt(num_square)

        if d > num_square + increased_num :
            count = 2 * num + 1
        elif d > num_square and d <= num_square + increased_num :
            count = 2 * num
        elif d == num_square :
            count = 2 * num - 1

        if d < 4 :
            count = d 
        print(count)
astronaut(num)
