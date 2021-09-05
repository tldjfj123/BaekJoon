n = int(input())
 
li = []

for i in range(n):
    li.append(list(map(int, input().split())))
 

for i in range(n):
    rank = 1
    for j in range(n):
        if i!=j:
            if (li[i][0] < li[j][0]) and (li[i][1] < li[j][1]):
                rank +=1
    print(rank,end=' ')