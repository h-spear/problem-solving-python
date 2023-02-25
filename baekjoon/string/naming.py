# https://www.acmicpc.net/problem/16900

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


s, k = input().split()
table = failure(s)
print(len(s) + (int(k) - 1) * (len(s) - table[-1]))
