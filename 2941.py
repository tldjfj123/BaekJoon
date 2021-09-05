# c= c- dz= d- lj nj s= z=
import re



str = input()

def croatia(s) :
    c_alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
    sum = 0
    for i in c_alpha :
        if len(re.findall(i, s)) > 0 :
            sum += len(re.findall(i,s ))
    return len(s) - sum

print(croatia(str))