import sys

def solution() :
    t = int(sys.stdin.readline())
    
    for _ in range(t) :
        sounds = sys.stdin.readline().rstrip().split()
        
        animals = []
        while 1 :
            s = sys.stdin.readline().rstrip().split()
            if s[-1] == 'say?' :
                for i in range(len(sounds)) :
                    if sounds[i] in animals :
                        sounds[i] = ''
                for s in sounds :
                    if s != '' :
                        print(s, end = ' ')
                break
            else :
                animals.append(s[-1])
                
solution()