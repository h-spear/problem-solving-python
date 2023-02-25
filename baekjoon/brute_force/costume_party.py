# https://www.acmicpc.net/problem/6159

n, s = map(int, input().split())
cows = []
for _ in range(n):
    cows.append(int(input()))

answer = 0
for i in range(n):
    for j in range(i + 1, n):
        if cows[i] + cows[j] <= s:
            answer += 1

print(answer)
