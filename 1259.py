while 1 :
    n = input()
    if n == '0' :
        break
    else :
        if n == ''.join(reversed(n)) :
            print("yes")
        else :
            print("no")