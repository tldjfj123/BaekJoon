def calendar() :
    d, m = map(int, input().split())
    
    date = ["Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday"]
    
    day = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]
    
    print(date[((day[m-1] + d) % 7)-1])

calendar()