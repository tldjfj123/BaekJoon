def prime_test(n) :
    for i in range(2, int(n**0.5) + 1) :
        if n % i == 0 :
            return "It is not a prime word."
    return "It is a prime word."

def prime() :
    s = input()
    
    sum = 0
    for i in s :
        if i.islower() == True :
            sum += ord(i)-96
        else :
            sum += ord(i)-38

    print(prime_test(sum))
    
prime()