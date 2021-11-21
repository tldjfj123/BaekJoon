import sys

def kem() :
    num = int(sys.stdin.readline())
    score = [list(sys.stdin.readline().split()) for _ in range(num)] 
    
    score = sorted(score, key = lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

    for i in score :
        print(i[0])
    
kem()