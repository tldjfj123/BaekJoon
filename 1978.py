num = int(input())
data = list(map(int, input().split()))

def is_prime_num(n):
    if n == 1 :
        return False
    for i in range(2, n):
        if n % i == 0:
            return False 
    return True 

def calc(data) :
    count = 0
    for i in range(len(data)) :
        if is_prime_num(data[i]) == True :
            count += 1
    return count

print(calc(data))