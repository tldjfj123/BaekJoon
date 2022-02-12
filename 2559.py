def solution() :
    n, k = map(int ,input().split())
    temp = list(map(int, input().split()))
    
    tmp = sum(temp[:k])
    prefix = [tmp]
    
    for i in range(len(temp)-k) :
        tmp = tmp - temp[i] + temp[i+k]
        prefix.append(tmp)
    
    print(max(prefix))
    
solution()