from collections import Counter

def solution() :
    colors = []
    numbers = []
    
    for _ in range(5) :
        color, number = input().split()
        colors.append(color)
        numbers.append(int(number))
    
    color_check = sorted(list(Counter(colors).values()))
    number_check = sorted(list(Counter(numbers).items()), key = lambda x : (-x[1], -x[0]))
    
    if color_check == [5] :
        if sorted(numbers, reverse = True) == sorted(numbers)[::-1] and (sorted(numbers)[0] + sorted(numbers)[-1]) / 2 == sorted(numbers)[2] :
            return max(numbers) + 900
        else :
            return max(numbers) + 600
    else :
        if number_check[0][1] == 4 :
            return number_check[0][0] + 800
        
        elif number_check[0][1] == 3 :
            if number_check[1][1] == 2 :
                return (number_check[0][0] * 10) + number_check[1][0] + 700
            else :
                return number_check[0][0] + 400
            
        elif number_check[0][1] == 2 :
            if number_check[1][1] == 2 :
                return (number_check[0][0] * 10) + number_check[1][0] + 300
            else :
                return number_check[0][0] + 200
            
        elif sorted(numbers, reverse = True) == sorted(numbers)[::-1] and (sorted(numbers)[0] + sorted(numbers)[-1]) / 2 == sorted(numbers)[2] :
            return max(numbers) + 500
        
        else :
            return max(numbers) + 100
            
print(solution())