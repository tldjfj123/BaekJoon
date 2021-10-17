def a_fib(num) :
    if num == 1 :
        return 0 
    else :
        res = []
        for i in range(num-1) :
            if i < 2 :
                res.append(1)
            else :
                res.append(res[i-2] + res[i-1])
        return res[-1]

def b_fib(num) :
    res = []
    for j in range(num) :
        if j < 2 :
            res.append(1)
        else :
            res.append(res[j-2] + res[j-1])
    return res[-1]

def babba() :
    num = int(input())
    print("{} {}".format(a_fib(num), b_fib(num)))
        
babba()