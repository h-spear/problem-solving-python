# https://www.acmicpc.net/problem/2776

from bisect import bisect_left, bisect_right


for tc in range(int(input())):
    n = int(input())
    memo1 = list(map(int, input().split()))
    m = int(input())
    memo2 = list(map(int, input().split()))

    memo1.sort()

    for x in memo2:
        ub = bisect_right(memo1, x)
        lb = bisect_left(memo1, x)

        if ub - lb >= 1:
            print(1)
        else:
            print(0)
