import sys

def one() :
    """
    1. 3으로 나뉘는 경우
    arr[n] = arr[n/3] + 1
    2. 2로 나뉘는 경우
    arr[n] = arr[n/2] + 1
    3. 1을 뺄 경우
    arr[n] = arr[n-1] + 1

    ex) n == 6
    arr[6] = arr[2] + 1 
    arr[6] = arr[3] + 1
    arr[6] = arr[5] + 1

    위 3개 식 중 최소값을 리턴하면 된다.
    arr[n] = min(arr[n/3], arr[n/2], arr[n-1]) + 1
    """

    num = int(sys.stdin.readline())
    arr = [0, 0, 1, 1]
    if num < 4 :
        print(arr[num])
    else :
        for i in range(4, num+1) :
            # 1을 빼주는 것을 전제로 +1 해줌
            arr.append(arr[i-1]+1)
            if i % 2 == 0 :
                arr[i] = min(arr[i], arr[i//2]+1)
            if i % 3 == 0 :
                arr[i] = min(arr[i], arr[i//3]+1)
    
        print(arr[-1])

one()

