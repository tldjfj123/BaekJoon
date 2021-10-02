def polynomio() :
    string = input()
    res = []
    count = 0
    if '.' not in string :
        string  = list(string)
        for s in string :
            if s == 'X' :
                count += 1

        if count % 2 != 0 :
            return -1

        elif count % 4 == 2 :
            for _ in range(count // 4) :
                res.append('AAAA')
            res.append('BB')

        elif count % 4 == 0 :
            for _ in range(count // 4) :
                res.append('AAAA')

        else :
            for _ in range(count // 2) :
                res.append('BB')

        result = ''.join(res)
        return result      

    else :
        dot = 0
        for s in string :
            if s == 'X' :
                count += 1
            else :
                dot += 1

            if dot == 1 :
                if count != 0 :
                    if count % 2 != 0 :
                        return -1

                    elif count % 4 == 2 :
                        for _ in range(count // 4) :
                            res.append('AAAA')
                        res.append('BB')
                        res.append('.')
                    elif count % 4 == 0 :
                        for _ in range(count // 4) :
                            res.append('AAAA')
                        res.append('.')
                    else :
                        res.append('BB')
                        res.append('.')
                else :
                    res.append('.')
                dot = 0
                count = 0
        
        if count > 0 :
            if count % 4 == 2 :
                for _ in range(count // 4) :
                    res.append('AAAA')
                res.append('BB')

            elif count % 4 == 0 :
                for _ in range(count // 4) :
                    res.append('AAAA')
            else :
                for _ in range(count // 2) :
                    res.append('BB')
            
        if count % 2 != 0 :
            return -1
        else :
            result = ''.join(res)
            return result
            
print(polynomio())