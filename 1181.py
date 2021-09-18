import sys

num = int(sys.stdin.readline())

def word(n) :
    wordlist = [sys.stdin.readline().rstrip() for _ in range(num)]
    wordlist = list(set(wordlist))
    wordlist.sort(key = lambda x : (len(x), x))
    for word in wordlist :
        print(word)

word(num)