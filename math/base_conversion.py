# https://www.acmicpc.net/problem/2745

N, B = input().split()
B = int(B)

_dict = dict()
for i in range(0, 10):
    _dict[str(i)] = i
for i in range(26):
    _dict[chr(i + 65)] = 10 + i

answer = 0
for i, x in enumerate(N):
    answer += _dict[x] * (B ** (len(N) - i - 1))

print(answer)
