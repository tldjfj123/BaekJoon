def calendar() :
    x, y = map(int, input().split())
    day = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    
    month = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]
    
    res = (month[x-1] + y) % 7
    
    print(day[res])  
    
calendar()