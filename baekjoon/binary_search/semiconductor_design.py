# https://www.acmicpc.net/problem/2352
# LIS

from bisect import bisect_left


def LIS_length(array):
    answer = 0
    dp = []
    for x in array:
        if not dp:
            dp.append(x)
            answer += 1
            continue

        if dp[-1] < x:
            dp.append(x)
            answer += 1
        else:
            index = bisect_left(dp, x)
            dp[index] = x
    return answer


n = int(input())
a = list(map(int, input().split()))
print(LIS_length(a))
