def chess() :
    m, n = map(int, input().split())
    board = []

    for _ in range(m) :
        board.append(list(input()))

    res = []
    # Count things need to be changed
    for start in range(n-7) :   # range of row
        for column_s in range(m-7) :    # range of column
            countB = 0
            countW = 0 
            countB2 = 0
            countW2 = 0

            # Start with 'B'
            for column in range(column_s, column_s + 8, 2) :   
                for i in range(start, start+8, 2) :
                    if board[column][i] != 'B' :
                        countB += 1
                for j in range(start+1, start+9, 2) :   
                    if board[column][j] != 'W' :
                        countW += 1
            for column in range(column_s+1, column_s+9, 2) :  
                for i in range(start, start+8, 2) :
                    if board[column][i] != 'W' :
                        countW += 1
                for j in range(start+1, start+9, 2) :
                    if board[column][j] != 'B' :
                        countB += 1

            # Start with 'W'
            for column in range(column_s, column_s + 8, 2) :
                for i in range(start, start+8, 2) :
                    if board[column][i] != 'W' :
                        countW2 += 1
                for j in range(start+1, start+9, 2) :
                    if board[column][j] != 'B' :
                        countB2 += 1

            for column in range(column_s+1, column_s+9, 2) :
                for i in range(start, start+8, 2) :
                    if board[column][i] != 'B' :
                        countB2 += 1
                for j in range(start+1, start+9, 2) :
                    if board[column][j] != 'W' :
                        countW2 += 1

            # Compare each option and append minimum 
            res.append((min((countB+countW), (countB2+countW2))))
    print(min(res))
chess()