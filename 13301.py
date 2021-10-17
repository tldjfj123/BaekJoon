def fib(num) :
    res = []
    for i in range(num) :
        if i < 2 :
            res.append(1)
        else :
            res.append(res[i-2] + res[i-1])
    return res[-1]

def tile() :
    num = int(input()) 
    res = 4
    for i in range(1, num) :
        res += 2*(fib(i+1))
    print(res)    

tile()