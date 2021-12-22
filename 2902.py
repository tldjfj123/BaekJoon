def kmp() :
    s = input().split('-')
    res = []
    
    for i in s :
        res.append(i[0])
    
    print(''.join(res))

kmp()