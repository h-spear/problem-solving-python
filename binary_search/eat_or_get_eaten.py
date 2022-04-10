# https://www.acmicpc.net/problem/7795

from bisect import bisect_right


for tc in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()

    i = 0
    answer = 0
    while i < n:
        j = bisect_right(a, a[i])
        cnt_a = j - i

        cnt_b = bisect_right(b, a[i] - 1)

        answer += cnt_a * cnt_b
        i = j

    print(answer)
