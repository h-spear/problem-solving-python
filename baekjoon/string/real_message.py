# https://www.acmicpc.net/problem/9324

from collections import defaultdict

for tc in range(int(input())):
    m = input()
    lm = len(m)
    _hash = defaultdict(int)
    flag = True

    i = 0
    while i < lm:
        char = m[i]
        _hash[char] += 1

        if _hash[char] == 3:
            if i + 1 == lm:
                flag = False
                break
            if i + 1 < lm and m[i + 1] != char:
                flag = False
                break
            _hash[char] = 0
            i += 2
            continue

        i += 1

    if flag:
        print("OK")
    else:
        print("FAKE")
