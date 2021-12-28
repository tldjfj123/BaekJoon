import sys

def cryptoqueue() :
    t = int(sys.stdin.readline())
    original = [chr(i) for i in range(65, 91)]

    for _ in range(t) :
        cyphertext = sys.stdin.readline().rstrip()
        key = list(sys.stdin.readline().rstrip())
        plaintext = []
        
        for c in cyphertext :
            if c == ' ' :
                plaintext.append(' ')
            else :    
                idx = original.index(c)
                plaintext.append(key[idx])
        
        print(''.join(plaintext))
        
cryptoqueue()