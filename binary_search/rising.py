# https://www.acmicpc.net/problem/3745

from bisect import bisect_left


def lis_length(arr):
    lis = 0
    dp = []
    for x in arr:
        if not dp:
            dp.append(x)
            lis += 1
            continue

        if dp[-1] < x:
            dp.append(x)
            lis += 1
        else:
            index = bisect_left(dp, x)
            dp[index] = x
    return lis


while 1:
    try:
        n = int(input())
        arr = list(map(int, input().split()))
        print(lis_length(arr))
    except:
        break
