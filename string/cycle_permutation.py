# https://www.acmicpc.net/problem/12104


def failure(string):
    table = [0] * len(string)
    j = 0
    for i in range(1, len(string)):
        while j > 0 and string[i] != string[j]:
            j = table[j - 1]

        if string[i] == string[j]:
            j += 1
            table[i] = j

    return table


def KMP(string, pattern):
    ls = len(string)
    lp = len(pattern)
    table = failure(pattern)
    j = 0
    cnt = 0
    for i in range(ls):
        while j > 0 and string[i] != pattern[j]:
            j = table[j - 1]

        if string[i] == pattern[j]:
            if j == lp - 1:
                cnt += 1
                j = table[j]
            else:
                j += 1
    return cnt


A = input()
B = input()
B *= 2
print(KMP(B[:-1], A))
