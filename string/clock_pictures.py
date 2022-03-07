# https://www.acmicpc.net/problem/10266


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
    for i in range(ls):
        while j > 0 and string[i] != pattern[j]:
            j = table[j - 1]

        if string[i] == pattern[j]:
            if j == lp - 1:
                return True
            else:
                j += 1

    return False


clock_1 = [0] * 360000
clock_2 = [0] * 360000

n = int(input())
t1 = list(map(int, input().split()))
for i in t1:
    clock_1[i] = 1

t2 = list(map(int, input().split()))
for i in t2:
    clock_2[i] = 1

clock_1 += clock_1

if not KMP(clock_1, clock_2):
    print("im", end="")
print("possible")
