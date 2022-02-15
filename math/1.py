while 1:
    try:
        n = int(input())

        cur = 1
        cnt = 1
        while 1:
            if cur % n == 0:
                print(cnt)
                break
            cur = cur * 10 + 1
            cnt += 1
    except:
        break
