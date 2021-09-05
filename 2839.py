weight = int(input())

def delivery(w) :
    result = []
    for i in range((w // 3) +1) :
        tmp1 = 3 * i
        for j in range((w // 5) + 1) :
            tmp2 = 5 * j
            if tmp1 + tmp2 == w :
                result.append(i+j)
    if len(result) == 0 :
        return -1
    else :
        return min(result)

print(delivery(weight))



    






