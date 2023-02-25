# https://www.acmicpc.net/problem/20164

from itertools import combinations


def counting_odd(num):
    cnt = 0
    for char in num:
        if int(char) & 1 == 1:
            cnt += 1
    return cnt


def fn(num, a=0, b=0):
    if len(num) == 1:
        return num
    elif len(num) == 2:
        return str(int(num[0]) + int(num[1]))

    return str(int(num[0:a]) + int(num[a:b]) + int(num[b:]))


def dfs(num, cnt):
    global _max, _min
    cnt += counting_odd(num)
    if len(num) == 1:
        _max = max(_max, cnt)
        _min = min(_min, cnt)
        return
    elif len(num) == 2:
        next = fn(num)
        dfs(next, cnt)
        return

    for a, b in combinations(range(1, len(num)), 2):
        next = fn(num, a, b)
        dfs(next, cnt)


_max, _min = -100000, 100000
n = input()
dfs(n, 0)
print(_min, _max)
