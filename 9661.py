def stone() :
    n = int(input())
    res = ['CY', 'SK', 'CY', 'SK', 'SK']
    
    print(res[n % 5])
    
stone()