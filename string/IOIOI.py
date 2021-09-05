# https://www.acmicpc.net/problem/5525

import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
m = int(input())
string = list(map(int, input().replace("I", "1").replace("O", "0")))

answer = 0
counter = 0
for i in range(len(string)):
    if string[i] == 0:
        if counter & 1 == 1 and string[i - 1] == 1:
            counter += 1
        else:
            counter = 0

    else:
        if counter == 0:
            counter = 1
        elif counter & 1 == 0 and string[i - 1] == 0:
            counter += 1
        else:
            counter = 1

        if counter == 2 * n + 1:
            answer += 1
            counter -= 2

print(answer)
