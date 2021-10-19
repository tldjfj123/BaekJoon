import sys

def foursquares() :
    num = int(sys.stdin.readline())
    # answer == 1
    if int(num ** 0.5) == num ** 0.5 :
        return 1 

    # answer == 2   
    for i in range(1, (int(num ** 0.5)) + 1) :
        if (num - (i ** 2)) ** 0.5 == int((num - (i ** 2)) ** 0.5) :
            return 2
    
    # answer == 3
    for i in range(1, (int(num ** 0.5)) + 1) :
        std = num - (i ** 2)
        for j in range(1, (int(std ** 0.5)) + 1) :
            if (std - (j ** 2)) ** 0.5 == int((std - (j ** 2)) ** 0.5) :
                return 3
    else :
        return 4

print(foursquares())