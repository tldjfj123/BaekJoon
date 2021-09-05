# .rjust(n) : n자리로 우측 정렬
# .ljust(n) : n자리로 좌측 정렬

num = int(input())

def star_r(n) :
    for i in range(n) :
        print(('*' * (i + 1)).rjust(n))

star_r(num)