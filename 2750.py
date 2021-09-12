num = int(input())
table = []

for _ in range(num) :
    i = int(input())
    table.append(i)

table.sort()

for integer in table :
    print(integer)