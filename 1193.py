import sys

num = int(sys.stdin.readline())

def fraction(n) :
    tmp = n
    count = 0
    sum = 0
    while 1 :
        count += 1
        n -= count
        if n <= 0 :
            break
        sum += count
    # count = 5
    # sum = 10
    if count % 2 == 1 :
        return "{}/{}".format((count + 1) - (tmp - sum) ,tmp - sum)
    else :
        return "{}/{}".format(tmp - sum, (count + 1) - (tmp - sum))

print(fraction(num))