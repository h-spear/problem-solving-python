# https://www.acmicpc.net/problem/5555

p = input()
n = int(input())
answer = 0
for _ in range(n):
    s = input()
    s += s
    if p in s:
        answer += 1

print(answer)
