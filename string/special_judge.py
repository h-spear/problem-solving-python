# https://www.acmicpc.net/problem/9253

# KMP
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


def KMP(string, pattern, table):
    ls = len(string)
    lp = len(pattern)

    j = 0
    for i in range(ls):
        while j > 0 and string[i] != pattern[j]:
            j = table[j - 1]

        if string[i] == pattern[j]:
            if j == lp - 1:
                return True
            j += 1
    return False


T = input()
S = input()
pattern = input()
table = make_table(pattern)
print("YES" if KMP(S, pattern, table) and KMP(T, pattern, table) else "NO")

# 간단하게
print(["NO", "YES"][(pattern in S) & (pattern in T)])
