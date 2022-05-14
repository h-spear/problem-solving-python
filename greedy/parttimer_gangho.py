# https://www.acmicpc.net/problem/1758

n = int(input())
tip = []
for _ in range(n):
    tip.append(int(input()))
tip.sort(reverse=True)

answer = 0
for i, x in enumerate(tip):
    answer += max(x - i, 0)

print(answer)
