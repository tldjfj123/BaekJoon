# 0 ~ 25
# 97 ~ 122

import re
import sys

str = input()

def ochk(arr) :
    std = max(arr)
    count = 0
    for i in arr :
        if i == std :
            count += 1
    if count > 1 :
        return True
    return False

def word(s) :
    s = s.lower()
    result = []
    for i in range(97, 123) :
        result.append(len(re.findall(chr(i), s)))
    if ochk(result) == True :
        return '?'
    return chr(result.index(max(result)) + 97).upper()

print(word(str))