def score() :
    k = int(input())
    
    idx = 1
    for _ in range(k) :
        arr = list(map(int, input().split()))
        student = arr[0]
        score = sorted(arr[1:])
        
        gap = 0
        for i in range(1, len(score)) :
            if score[i] - score[i-1] >= gap :
                gap = score[i] - score[i-1]
            
        
        print(f"Class {idx}")
        print(f"Max {max(score)}, Min {min(score)}, Largest gap {gap}")
        idx += 1
        
score()