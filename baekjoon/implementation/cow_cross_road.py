# https://www.acmicpc.net/problem/14467

n = int(input())

answer = 0
cow = [-1] * 11
for _ in range(n):
    n, pos = map(int, input().split())

    if cow[n] == -1:
        cow[n] = pos
    elif cow[n] != pos:
        cow[n] = pos
        answer += 1

print(answer)
