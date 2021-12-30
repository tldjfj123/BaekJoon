def diary() :
    vowel = ["a", "e", "i", "o", "u"]
    s = list(input())
    
    for i in range(1, len(s)) :
        if s[i-1] in vowel :
            s[i] = ""
            s[i+1] = ""
    
    print(''.join(s))
        
diary()