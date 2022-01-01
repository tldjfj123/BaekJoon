from collections import deque
import sys

def romanToInt(s: str) -> int :
    table = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
    
    fin = 0
    
    if len(s) >= 2 :
        s = deque(list(s))
        
        while len(s) != 0 :
            if s[0] == 'I' :
                if len(s) > 1 :
                    if s[1] == 'V' :
                        fin += 4
                        s.popleft()
                        s.popleft()
                    elif s[1] == 'X' :
                        fin += 9
                        s.popleft()
                        s.popleft()
                    else :
                        fin += table[s[0]]
                        s.popleft()
                else :
                    fin += table[s[0]]
                    s.popleft()
            elif s[0] == 'X' :
                if len(s) > 1 :
                    if s[1] == 'L' :
                        fin += 40
                        s.popleft()
                        s.popleft()
                    elif s[1] == 'C' :
                        fin += 90
                        s.popleft()
                        s.popleft()
                    else :
                        fin += table[s[0]]
                        s.popleft()
                else :
                    fin += table[s[0]]
                    s.popleft()
            elif s[0] == 'C' :
                if len(s) > 1 :      
                    if s[1] == 'D' :
                        fin += 400
                        s.popleft()
                        s.popleft()
                    elif s[1] == 'M' :
                        fin += 900
                        s.popleft()
                        s.popleft()
                    else :
                        fin += table[s[0]]
                        s.popleft()
                else :
                    fin += table[s[0]]
                    s.popleft()
            else :
                fin += table[s[0]]
                s.popleft()
        
        return fin
    else :
        return table[s]

def intToRoman(i = int) -> str :
    table = {1 : 'I', 4 : 'IV', 5 : 'V', 9 : 'IX', 10 : 'X', 40 : 'XL', 50 : 'L', 90 : 'XC', 100 : 'C', 400 : 'CD', 500 : 'D', 900 : 'CM', 1000 : 'M'}
    i = str(i)
    
    s = []
    for f in range(len(i)) :
        if i[f] == '4' or i[f] == '9' :
            s.append(int(i[f]) * (10 **  (len(i)-f-1)))
        else :
            if int(i[f]) >= 5 :
                s.append(5 * (10 **  (len(i)-f-1)))
                leftover = int(i[f]) - 5
                
                for j in range(leftover) :
                    s.append((10 **  (len(i)-f-1)))
            else :
                for j in range(int(i[f])) :
                    s.append((10 **  (len(i)-f-1)))
                
    res = []
    
    for i in s :
        res.append(table[i])
    
    return ''.join(map(str, res))
           
def main() :
    s1 = sys.stdin.readline().rstrip()
    s2 = sys.stdin.readline().rstrip()
    
    calc = romanToInt(s1) + romanToInt(s2)
    
    print(calc)
    print(intToRoman(calc))

main()