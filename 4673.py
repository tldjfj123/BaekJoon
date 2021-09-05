def self(n) :
    sum = 0
    for j in range(len(str(n))) :
        sum += int(str(n)[j])
    sum += int(n)
    return sum

def calc() :
    comp = []
    for i in range(1, 10001) :
        comp.append(self(i))
    for j in range(1, 10001) :
        if j not in comp :
            print(j)

calc()