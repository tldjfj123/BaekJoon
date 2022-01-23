def laydown() :
    n = int(input())
    room = [list(input()) for _ in range(n)]
    
    # row
    row_count = 0
    for i in range(n) :
        count = 0
        for j in range(n) :
            if room[i][j] == '.' :
                count += 1
            else :
                count = 0
            if count == 2 :
                row_count += 1
    
    # column
    column_count = 0
    for i in range(n) :
        count = 0
        for j in range(n) :
            if room[j][i] == '.' :
                count += 1
            else :
                count = 0
            
            if count == 2 :
                column_count += 1

    print(row_count, column_count)

laydown()