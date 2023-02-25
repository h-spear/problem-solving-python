# https://www.acmicpc.net/problem/17609


def check(string, _from):
    i = 0
    j = n - 1

    result = 0
    while i < j:
        if string[i] == string[j]:
            i += 1
            j -= 1
        elif result == 0:
            if _from == 0:
                i += 1
            else:
                j -= 1
            result = 1
        elif result == 1:
            result = 2
            break
    return result


for t in range(int(input())):
    string = input()
    n = len(string)

    print(min(check(string, 0), check(string, 1)))
