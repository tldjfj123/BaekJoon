num = int(input())

def ATM(n) :
    time = list(map(int, input().split()))
    time.sort()
    total = 0
    for i in range(1, len(time) + 1) :
        total += sum(time[:i])
    return total

print(ATM(num))



# 메모리 초과로 실패
# from itertools import permutations

# num = int(input())

# def ATM(n) :
#     time = list(map(int, input().split()))
#     cases = list(permutations(time, 5))
#     time_result = []
#     case_result = []
#     for case in cases :
#         total = 0
#         for i in range(1, len(case) + 1) :
#             total += sum(case[:i])
#     return min(time_result), case_result, time_result

# print(ATM(num))

