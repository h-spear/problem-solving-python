# https://www.acmicpc.net/problem/7575

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


n, k = map(int, input().split())
programs = []
for _ in range(n):
    _ = int(input())
    programs.append(list(input().split()))

programs.sort(key=len)

for i in range(len(programs[0]) - k + 1):
    pattern = " ".join(programs[0][i : i + k])
    pattern_rev = " ".join(programs[0][i : i + k][::-1])
    table = failure(pattern)
    table_rev = failure(pattern_rev)
    cnt = 0
    for idx, program in enumerate(programs):
        if idx == 0:
            continue

        string = " ".join(program)
        if (
            KMP(string, pattern, table) == False
            and KMP(string, pattern_rev, table_rev) == False
        ):
            break

        cnt += 1
        if cnt == len(programs) - 1:
            print("YES")
            sys.exit()

print("NO")
