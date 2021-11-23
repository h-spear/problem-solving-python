# https://www.acmicpc.net/problem/13410

n, k = map(int, input().split())

answer = 0
for i in range(1, k + 1):
    mul = list(str(n * i))
    mul.reverse()
    mul = int("".join(mul))
    answer = max(answer, mul)

print(answer)
