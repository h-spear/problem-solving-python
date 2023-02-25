# https://www.acmicpc.net/problem/2740

A = []
B = []

N, M = map(int, input().split())
for _ in range(N):
    A.append(list(map(int, input().split())))

M, K = map(int, input().split())
for _ in range(M):
    B.append(list(map(int, input().split())))

answer = [[0] * K for _ in range(N)]
for i in range(N):
    for j in range(K):
        temp = 0
        for k in range(M):
            temp += A[i][k] * B[k][j]
        answer[i][j] = temp

for x in answer:
    print(*x)
