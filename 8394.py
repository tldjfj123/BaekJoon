import sys

def handshake() :
    num = int(sys.stdin.readline())
    
    result, plus = 1, 0
    
    for _ in range(num) :
        result, plus = int(str(result + plus)[-1]), int(str(result)[-1])

    print(result)
    
handshake()