a, b = map(int, input().split())

def gcd(a, b) :
    r = a % b
    if r == 0 :
        return b
    else :
        return gcd(b, r)

def lcm(a, b) :
    count  = 0
    while 1 :
        count += 1
        if count * a % b == 0 :
            return count * a

def main(a, b) :
    print(gcd(a, b))
    print(lcm(a, b))

main(a, b)