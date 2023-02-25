# https://www.acmicpc.net/problem/14425

n, m = map(int, input().split())
S = set(input() for _ in range(n))
answer = 0
for _ in range(m):
    string = input()
    if string in S:
        answer += 1

print(answer)
