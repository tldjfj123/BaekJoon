def solution() :
    n = int(input())
    trees = sorted(list(map(int, input().split())), reverse = True)
    
    for i in range(n) :
        trees[i] = trees[i] + i + 1
    
    print(max(trees) + 1)           
            
solution()