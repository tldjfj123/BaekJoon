from itertools import permutations

def calc() :
    n = int(input())
    nums = list(map(int, input().split()))
    tmp = list(map(int, input().split()))
    op = []
    for i in range(len(tmp)) :
        if i == 0 :
            for _ in range(tmp[i]) :
                op.append('+')
        elif i == 1 :
            for _ in range(tmp[i]) :
                op.append('-')
        elif i == 2 :
            for _ in range(tmp[i]) :
                op.append('*')
        else :
            for _ in range(tmp[i]) :
                op.append('/')        
    
    per = list(map(lambda x : list(x), permutations(op, sum(tmp))))

    res = []
    for p in per :
        tmp = nums[0]
        for i in enumerate(p, start = 1) :
            if i[1] == '+' :
                tmp += nums[i[0]]
            elif i[1] == '-' :
                tmp -= nums[i[0]]
            elif i[1] == '*' :
                tmp *= nums[i[0]]
            else :
                if tmp < 0 :
                    tmp = -(-tmp // nums[i[0]])
                else :
                    tmp //= nums[i[0]]
        res.append(tmp)
    
    print(max(res))
    print(min(res))
            
calc()