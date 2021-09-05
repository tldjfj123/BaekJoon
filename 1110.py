num = input()

def cycle(n) :
    count = 0
    std = n
    while 1 :
        n_list = list(n)
        if len(n_list) == 1 :
            n_list.insert(0, str(0))
        tmp = [n_list[1], str(int(n_list[0]) + int(n_list[1]))]
        count += 1
        if len(tmp[1]) > 1 and tmp[1] != '00' :
            tmp = [n_list[1], tmp[1][1]]
            n = ''.join(tmp)
        n = ''.join(tmp)
        if int(std) == int(n) :
            print(count)
            return count
cycle(num)