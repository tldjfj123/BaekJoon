import sys
import math

def find() :
    n = int(sys.stdin.readline())
    n_list = list(map(int, sys.stdin.readline().split()))
    m = int(sys.stdin.readline())
    m_list = list(map(int, sys.stdin.readline().split()))

    n_list.sort()

    if n >= 3 :
        for factor in m_list :

            left = 0
            right = n-1
            res = 0

            while left <= right :
                mid = (left + right) // 2

                if n_list[mid] == factor :
                    res = 1
                    break
                elif n_list[mid] > factor :
                    right = mid - 1
                else :
                    left = mid + 1

            if res == 0 :
                print(0)
            else :
                print(1)
    else :
        for factor in m_list :
            if factor in n_list :
                print(1)
            else :
                print(0)
        
find()