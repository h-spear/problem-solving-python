# https://www.acmicpc.net/problem/1644

n = int(input())
A = [True] * (n + 5)

A[0], A[1] = False, False
for i in range(2, int(n ** 0.5) + 1):
    if A[i] == True:
        # i가 소수인 경우 i를 제외한 i의 모든 배수 false
        j = 2
        while i * j <= n:
            A[i * j] = False
            j += 1

prime = [i for i, bool in enumerate(A) if bool]

lp = len(prime)
i = 0
j = 1
curr_sum = prime[i]
cnt = 0
while i < j:
    if curr_sum == n:
        cnt += 1
        curr_sum -= prime[i]
        i += 1

    if j == lp and curr_sum < n:
        break
    elif curr_sum < n:
        curr_sum += prime[j]
        j += 1
    elif curr_sum > n:
        curr_sum -= prime[i]
        i += 1

print(cnt)
