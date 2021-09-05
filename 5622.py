str = input()

def dial(s) :
    table = {3 : ['A', 'B', 'C'], 4 : ['D', 'E', 'F'], 5 : ['G', 'H', 'I'], 6 : ['J', 'K', 'L'], 7 : ['M', 'N', 'O'], 8 : ['P', 'Q', 'R', 'S'], 9 : ['T', 'U', 'V'], 10 : ['W', 'X', 'Y', 'Z']}
    sum = 0
    for i in range(len(s)) :    # 문자에 대해서
        for j in range(len(table.keys())) :
            if s[i] in table[j+3] :
                sum += (j+3)
    return sum

print(dial(str))

