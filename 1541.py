form = input()

def calc(f) :
    tmp = f.split('-')

    filtered = []

    for i in tmp :
        if '+' in i :
            tmp2 = list(map(int, i.split('+')))
            filtered.append(sum(tmp2))
        else :
            filtered.append(int(i))
    print(filtered[0] - sum(filtered[1:]))

calc(form)