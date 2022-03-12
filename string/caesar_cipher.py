# https://www.acmicpc.net/problem/1893

import sys

input = lambda: sys.stdin.readline().rstrip()


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


def KMP(cipher_text, plain_text, hash):
    table = failure(plain_text)
    ls = len(cipher_text)
    lp = len(plain_text)
    j = 0
    cnt = 0
    for i in range(ls):
        while j > 0 and cipher_text[i] != hash[plain_text[j]]:
            j = table[j - 1]

        if cipher_text[i] == hash[plain_text[j]]:
            if j == lp - 1:
                cnt += 1
                if cnt == 2:
                    return False
                j = table[j]
            else:
                j += 1
    return True if cnt == 1 else False


for tc in range(int(input())):
    alphabet = input()
    plain_text = input()
    cipher_text = input()

    answer = []
    for shift in range(len(alphabet)):

        hash = {}
        for i, x in enumerate(alphabet):
            hash[x] = alphabet[(i + shift) % len(alphabet)]

        if KMP(cipher_text, plain_text, hash):
            answer.append(shift)

    answer.sort()
    if len(answer) == 0:
        print("no solution")
        continue
    elif len(answer) == 1:
        print("unique: ", end="")
    else:
        print("ambiguous: ", end="")
    print(*answer)
