# https://www.acmicpc.net/problem/11728

n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

i, j = 0, 0
C = []
while i < n and j < m:
    if A[i] < B[j]:
        C.append(A[i])
        i += 1
    else:
        C.append(B[j])
        j += 1

while i < n:
    C.append(A[i])
    i += 1

while j < m:
    C.append(B[j])
    j += 1

print(*C)
