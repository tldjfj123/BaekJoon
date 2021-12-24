def calc() :
    n = int(input())
    arr = list(map(int, input().split()))
    
    stack = []
    score = 0
    for i in range(len(arr)) :
        if arr[i] == 1 :
            stack.append(1)
            score += sum(stack)
        else :
            stack = []
    
    print(score)
            
calc()