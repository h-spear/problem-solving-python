# https://www.acmicpc.net/problem/17298

n = int(input())
A = list(map(int, input().split()))
stack = []
answer = [-1] * n
for i in range(n):
    while stack and A[stack[-1]] < A[i]:
        curr = stack.pop()
        answer[curr] = A[i]

    stack.append(i)

print(*answer)
