import sys

def solution() :
    s = sys.stdin.readline().rstrip()
    res = []
    
    for s in s :
        if ord(s) in range(65, 91) :
            if ord(s) + 13 > 90 :
                res.append(chr(ord(s) - 13))
            else :
                res.append(chr(ord(s) + 13))
        elif ord(s) in range(97, 123) :
            if ord(s) + 13 > 122 :
                res.append(chr(ord(s) - 13))
            else :
                res.append(chr((ord(s) + 13)))
        else :
            res.append(str(s))

    print(''.join(res))
    
solution()