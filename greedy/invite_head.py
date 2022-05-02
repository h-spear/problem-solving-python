# https://www.acmicpc.net/problem/9237

n = int(input())
t = list(map(int, input().split()))
t.sort(reverse=True)

answer = 0
for i, x in enumerate(t):
    answer = max(answer, x + i + 2)

print(answer)
