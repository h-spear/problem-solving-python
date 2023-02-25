# https://www.acmicpc.net/problem/11508

n = int(input())
c = [int(input()) for _ in range(n)]
c.sort()

answer = 0
while len(c) >= 3:
    c1 = c.pop()
    c2 = c.pop()
    c3 = c.pop()
    answer += c1
    answer += c2

answer += sum(c)
print(answer)
