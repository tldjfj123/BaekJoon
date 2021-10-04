note = list(map(int, input().split()))

def music(n) :
    a = [1, 2, 3, 4, 5, 6, 7, 8]
    d = [8, 7, 6, 5, 4, 3, 2, 1]

    if n == a :
        print("ascending")
    elif n == d :
        print("descending")
    else :
        print("mixed")

music(note)