# https://www.acmicpc.net/problem/13506
# prefix이면서 suffix 인 것은 fail(S), fail(fail(S)), fail(fail(fail(S))) ...


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
                if cnt >= 3:
                    return True
            else:
                j += 1
    return False


def solution(string):
    table = failure(string)
    while table[-1]:
        pattern = string[: table[-1]]
        if KMP(string, pattern):
            print(pattern)
            return
        table = failure(pattern)

    print(-1)


string = input()
solution(string)
