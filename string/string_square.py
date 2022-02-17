# https://www.acmicpc.net/problem/4354


def failure(pattern):
    table = [0] * len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = table[j - 1]

        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j

    div, mod = divmod(len(pattern), len(pattern) - table[-1])
    if mod != 0:
        return 1
    else:
        return div


while 1:
    s = input()
    if s == ".":
        break
    print(failure(s))
