# https://www.acmicpc.net/problem/1431

from functools import cmp_to_key


def compare(a, b):
    la = len(a)
    lb = len(b)
    if la < lb:
        return -1
    elif la > lb:
        return 1

    l = la
    s_a, s_b = 0, 0
    for i in range(l):
        if a[i].isdigit():
            s_a += int(a[i])
        if b[i].isdigit():
            s_b += int(b[i])

    if s_a < s_b:
        return -1
    elif s_a > s_b:
        return 1

    if a < b:
        return -1
    else:
        return 1


n = int(input())
words = [input() for _ in range(n)]
words.sort(key=cmp_to_key(compare))

for word in words:
    print(word)
