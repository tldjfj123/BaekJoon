a = int(input())
b = int(input())
c = int(input())

def calc(a, b, c) :
    value = str(a * b * c)
    for i in range(10) :
        print(value.count(str(i)))

calc(a, b, c)