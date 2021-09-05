import sys

num = int(sys.stdin.readline())

def quiz(n) :
    sheet = [list(input()) for i in range(num)]
    for i in range(len(sheet)) :
        final_score = 0
        mid_score = 0
        for j in range(len(sheet[i])) :
            if sheet[i][j] == 'O' :
                mid_score += 1
            elif sheet[i][j] == 'X' :
                mid_score = 0
            final_score += mid_score
        print(final_score)    

quiz(num)


    

 

