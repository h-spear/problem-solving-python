# https://www.acmicpc.net/problem/1786


def make_table(pattern):
    pattern_size = len(pattern)
    table = [0] * pattern_size
    j = 0
    for i in range(1, pattern_size):
        while j > 0 and pattern[i] != pattern[j]:
            j = table[j - 1]

        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j

    return table


def KMP(parent, pattern):
    table = make_table(pattern)
    result = []
    j = 0
    for i in range(len(parent)):
        while j > 0 and parent[i] != pattern[j]:
            j = table[j - 1]

        if parent[i] == pattern[j]:
            if j == len(pattern) - 1:
                result.append(i - len(pattern) + 2)
                j = table[j]
            else:
                j += 1
    print(len(result))
    for x in result:
        print(x)


parent = input()
pattern = input()
KMP(parent, pattern)
