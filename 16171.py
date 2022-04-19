def solution() :
    s = list(input())
    k = input()
    
    filtered = []
    
    for s in s :
        if s.isalpha() == True :
            filtered.append(s)
    
    filtered = ''.join(filtered)
    
    if k in filtered :
        print(1)
    else :
        print(0)

solution()