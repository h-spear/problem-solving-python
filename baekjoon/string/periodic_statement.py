# https://www.acmicpc.net/problem/1498


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


def print_i_n(table):
    for i in range(len(table)):
        if table[i] == 0:
            continue
        if (i + 1) % (i + 1 - table[i]) != 0:
            continue
        print(i + 1, (i + 1) // (i + 1 - table[i]))


s = input()
table = failure(s)
print_i_n(table)
