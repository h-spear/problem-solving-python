# https://www.acmicpc.net/problem/10973

n = int(input())
a = list(map(int, input().split()))


def prev_permutation(a):
    pp = a.copy()

    j = -1
    for i in range(n - 1, 0, -1):
        if pp[i - 1] > pp[i]:
            j = i - 1
            break

    if j == -1:
        return None

    for i in range(n - 1, 0, -1):
        if pp[i] < pp[j]:
            pp[j], pp[i] = pp[i], pp[j]
            pp = pp[: j + 1] + sorted(pp[j + 1 :], reverse=True)
            return pp


pp = prev_permutation(a)
if pp:
    print(*pp)
else:
    print(-1)
