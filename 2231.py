num = int(input())

def decom(n) :
    for i in range(n) :
        tmp = 0
        for j in range(len(str(i))) :
            tmp += int(str(i)[j])
        if i + tmp == n :
            return i
    return 0

print(decom(num))