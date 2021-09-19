list = list(map(int, input().split()))
sum = 0

for l in list :
    sum += (l ** 2)

print(sum % 10)