# https://www.acmicpc.net/problem/3356


def failure(pattern):
    table = [0] * len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = table[j - 1]

        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j
    return table


n = int(input())
s = input()
table = failure(s)
print(n - table[-1])
