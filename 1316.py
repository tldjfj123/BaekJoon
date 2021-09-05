# 97 ~ 122

num = int(input())

def check(n) :
    word = [input() for i in range(n)]
    count = 0
    for w in word :
        error = 0
        if len(w) == len(set(w)) :
            count += 1
            continue
        for j in range(len(w)-1) :
            if w[j] in w[j+1:] :
                if w[j] != w[j+1] :
                    error += 1
                    continue
        if error == 0 :
            count += 1
        
    return count      

print(check(num))