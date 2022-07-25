# https://www.acmicpc.net/problem/10972

n = int(input())
a = list(map(int, input().split()))


def next_permutation(a):
    np = a.copy()

    j = -1
    for i in range(n - 1, 0, -1):
        if np[i - 1] < np[i]:
            j = i - 1
            break

    if j == -1:
        return None

    for i in range(n - 1, 0, -1):
        if np[i] > np[j]:
            np[j], np[i] = np[i], np[j]
            np = np[: j + 1] + sorted(np[j + 1 :])
            return np


np = next_permutation(a)
if np:
    print(*np)
else:
    print(-1)
