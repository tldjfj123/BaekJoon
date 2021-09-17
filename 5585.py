num = int(input())
coin = [500, 100, 50, 10, 5, 1]

def change(n) :
    count = 0
    left = 1000 - n
    for c in coin :
        if left // c > 0 :
            count += left // c
            left = left % c
    print(count)


change(num)