from itertools import combinations

num, std = map(int, input().split())

arr = list(map(int, input().split()))

def blackjack(n, s) :
    tmp = list(combinations(arr, 3))
    new_std = list(map(sum, tmp))
    new_std.sort(reverse = True)
    
    for i in new_std :
        if i <= s :
            return i

print(blackjack(num, std))
