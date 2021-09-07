import sys

n, k = map(int, sys.stdin.readline().split())

def coin(n, k) :
    price = []
    for _ in range(n) :
        price.append(int(sys.stdin.readline()))
    price.sort(reverse=True)

    count = 0
    
    for money in price :
        if money > k :
            continue
        if k // money > 0 :
            count += (k // money)
            k = k % money

    return count

print(coin(n, k))