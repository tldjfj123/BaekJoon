import  sys

def card() :
    n = int(sys.stdin.readline())
    n_list = list(map(int, sys.stdin.readline().split()))
    m = int(sys.stdin.readline())
    m_list = list(map(int, sys.stdin.readline().split()))

    overlap = {}
    for n in n_list :
        try : overlap[n] += 1
        except : overlap[n] = 1

    n_list = list(set(n_list))

    n_list.sort()
    n = len(n_list)
    result = []

    for factor in m_list :
        left = 0
        right = n-1
        res = 0

        while left <= right :
            mid =  (left + right) // 2
            if n_list[mid] == factor :
                res = 1
                break
            elif n_list[mid] > factor :
                right = mid - 1
            else :
                left = mid + 1
    
        if res == 1 :
            result.append(overlap[factor])
        else :
            result.append(0)

    print(' '.join(list(map(str, result))))

card()