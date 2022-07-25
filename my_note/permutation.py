# next permutation 알고리즘
# https://velog.io/@wlrhkd49/%EB%B0%B1%EC%A4%80-10972-%EB%8B%A4%EC%9D%8C-%EC%88%9C%EC%97%B4-Python
# https://www.acmicpc.net/problem/10972


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


# prev permutation은 next permutation의 완전 반대 과정
# https://www.acmicpc.net/problem/10973


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


n = 5
a = [1, 2, 5, 4, 3]
np = next_permutation(a)
pp = prev_permutation(a)

print(np)
print(pp)
