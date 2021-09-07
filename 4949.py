import sys

def balance() :
    while 1 :
        check = 0
        table = []
        s = sys.stdin.readline().rstrip()
        if s == '.' :
            break

        for word in s :
            if word == '(' :
                table.append(word)
            if word == '[' :
                table.append(word)

            if word == ')' :
                if len(table) == 0 :
                    print("no")
                    check += 1
                    break
                elif table[-1] == '(' :
                    table.pop()
                elif table[-1] == '[' :
                    print("no")
                    check += 1
                    break
 
            if word == ']' :
                if len(table) == 0 :
                    print("no")
                    check += 1
                    break
                elif table[-1] == '[' :
                    table.pop()
                elif table[-1] == '(' :
                    print("no")
                    check += 1
                    break
        if check == 0 and len(table) == 0 :
            print("yes")
        if len(table) != 0 and check == 0 :
            print("no")
        else :
            pass
        

balance()
