num = int(input())

def doom(n) :
    i = 0
    count = 0
    while count <= n-1 :
        i += 1
        if "666" in str(i) :
            count += 1
    print(i)

doom(num)