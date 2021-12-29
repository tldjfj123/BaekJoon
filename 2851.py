def mario() :
    score = []
    for _ in range(10) :
        score.append(int(input()))
    
    total = []
    for i in range(len(score)) :
        total.append((abs(sum(score[:i+1]) - 100), sum(score[:i+1])))

    total.sort(key = lambda x : (x[0], -x[1]))
        
    print(total[0][1])
        
mario()