# 개행 없이 출력 >> print(출력 대상, end = "") (""사이에 간격을 주면 띄어져 출력됨. )

import sys

num, std = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

result = []

def calc(s) :
    for i in range(len(arr)) :
        if arr[i] < s :
            result.append(arr[i])
    
    for i in result :
        print(i, end = ' ')


calc(std)