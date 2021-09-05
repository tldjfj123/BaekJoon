# ASCII : 97 ~ 122

string = list(input())

def search(str) :
    res = []
    for i in range(97, 123) :
        if chr(i) in str :
            res.append(str.index(chr(i)))
        else :
            res.append(-1)
    for i in range(len(res)) :
        print(res[i] , end = ' ')

search(string)