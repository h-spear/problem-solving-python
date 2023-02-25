# https://www.acmicpc.net/problem/1365

from bisect import bisect_left


def LIS_length(array):
    result = 0
    dp = []
    for x in array:
        if not dp:
            dp.append(x)
            result += 1
            continue

        if dp[-1] < x:
            dp.append(x)
            result += 1
        else:
            index = bisect_left(dp, x)
            dp[index] = x
    return result


n = int(input())
a = list(map(int, input().split()))
print(n - LIS_length(a))
