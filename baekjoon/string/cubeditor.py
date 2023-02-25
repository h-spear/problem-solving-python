# https://www.acmicpc.net/problem/1701


def failure(pattern):
    global answer
    lp = len(pattern)
    table = [0] * lp

    j = 0
    for i in range(1, lp):
        while j > 0 and pattern[i] != pattern[j]:
            j = table[j - 1]

        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j

    answer = max(answer, max(table))


answer = 0
string = input()
for i in range(len(string)):
    failure(string[i:])

print(answer)
