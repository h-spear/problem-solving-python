# https://www.acmicpc.net/problem/6613


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


def KMP(string, pattern, table):
    ls = len(string)
    lp = len(pattern)
    temp = ""
    k = 0
    while 1:
        j = 0
        finded = False
        for i in range(k, ls):
            while j > 0 and string[i] != pattern[j]:
                j = table[j - 1]

            if string[i] == pattern[j]:
                if j == lp - 1:
                    temp = string[: i - lp + 1]
                    temp += string[i + 1 :]
                    finded = True
                    k = max(0, i - 2 * lp)
                    ls = len(temp)
                    break
                else:
                    j += 1

        if not finded:
            return string

        string = temp


while 1:
    try:
        t, b = input().split()
        table = failure(b)
        for _ in range(int(t)):
            string = input()
            print(KMP(string, b, table))
    except:
        break
