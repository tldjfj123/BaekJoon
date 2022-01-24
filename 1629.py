a, b, c = map(int, input().split())

def solution(a, b) :
    if b == 1 :
        return a % c
    else :    
        calc = solution(a, b // 2)
        if b % 2 == 0 :
            return (calc * calc % c)
        else :
            return ((calc * calc * a) % c)
    
print(solution(a, b))