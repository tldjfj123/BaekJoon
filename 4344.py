import sys

num = int(sys.stdin.readline())

def average(n) :
    sheet = [list(map(int, input().split())) for i in range(n)]
    for i in range(len(sheet)) :
        std = float(sum(sheet[i][1:]) / sheet[i][0])
        result = []
        for j in range(1, len(sheet[i])) :  
            if sheet[i][j] > std :
                result.append(sheet[i][j])
        print('%.3f' %round((len(result) / sheet[i][0]) * 100, 3) + '%')
        result = []

average(num)   