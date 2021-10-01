number = int(input())

def section(num) :
    arr = list(map(int, input().split()))
    n = int(input())

    arr.sort()

    for a in arr :
        if a == n :
            return 0

    if min(arr) > n :
        table1 = [i for i in range(1, min(arr))]
        res1 = 0
        for i in range(len(table1)-1) :
            for j in range(i+1, len(table1)) :
                if n in range(table1[i], table1[j]+1) :
                    res1 += 1
        return res1

    else :
        for i in range(num-1) :
            if n in range(arr[i]+1, arr[i+1]) :
                s_idx = arr[i] + 1
                f_idx = arr[i+1]
                break
        res2 = 0
        table2 = [i for i in range(s_idx, f_idx)]
 
        for i in range(len(table2)-1) :
            for j in range(i+1, len(table2)) :
                if n in range(table2[i], table2[j]+1) :
                    res2 += 1
        return res2

print(section(number))