def change() :
    n = int(input())

    if n == 1 or n == 3 :
        return -1

    if n % 5 == 0 :
        return n // 5
    else :
        if n % 5 == 1 or n % 5 == 3 :
            calc = (n // 5)-1
        else :
            calc = n // 5
        return calc + (n - (5 * calc))//2

print(change())