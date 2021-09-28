num = input()

def room(n) :
    r = list(n)
    count = 1 # default 
    reserve = [1 for _ in range(10)]

    for num in r :
        if num == '6' :
            if reserve[int(num)] >= 1 :
                reserve[int(num)] -= 1
            else :
                if reserve[9] >= 1 :
                    reserve[9] -= 1
                else :
                    count += 1
                    reserve = [r+1 for r in reserve]
                    reserve[int(num)] -= 1
        elif num == '9' :
            if reserve[int(num)] >= 1 :
                reserve[int(num)] -= 1
            else :
                if reserve[6] >= 1 :
                    reserve[6] -= 1
                else :
                    count += 1
                    reserve = [r+1 for r in reserve]
                    reserve[int(num)] -= 1
        else :
            if reserve[int(num)] >= 1 :
                reserve[int(num)] -= 1
            else :
                count += 1
                reserve = [r+1 for r in reserve]
                reserve[int(num)] -= 1
    print(count)                

room(num) 