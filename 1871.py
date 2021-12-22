def nice() :
    n = int(input())
    
    for _ in range(n) :
        plate = input().split("-")
        front = ((ord(plate[0][0])-65) * (26 ** 2)) + ((ord(plate[0][1])-65) * 26) + ord(plate[0][2])-65
        back = int(plate[1])
        
        if abs(front - back) <= 100 :
            print("nice")
        else :
            print("not nice")

nice()