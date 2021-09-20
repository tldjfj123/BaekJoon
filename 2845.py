num, people = map(int, input().split())

def calc(n, p) :
    total = list(map(int, input().split()))
    for t in total :
        print(t - p*n, end = ' ')

calc(num, people)