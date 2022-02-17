# https://www.acmicpc.net/problem/1305


def make_table(pattern):
    table = [0] * len(pattern)

    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = table[j - 1]

        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j

    return table


l = int(input())
pattern = input()
table = make_table(pattern)
print(l - table[l - 1])
