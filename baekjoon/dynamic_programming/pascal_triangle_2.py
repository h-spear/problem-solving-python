# https://www.acmicpc.net/problem/15489


q = 50
comb = [[0] * q for _ in range(q)]
for i in range(q):
    comb[i][0] = 1
    comb[i][i] = 1

for i in range(q):
    for j in range(1, i):
        comb[i][j] = comb[i - 1][j - 1] + comb[i - 1][j]


r, c, w = map(int, input().split())
curr = 0
answer = 0
for j in range(c - 1, c + w - 1):
    for i in range(r - 1 + curr, r + w - 1):
        answer += comb[i][j]
    curr += 1

print(answer)
