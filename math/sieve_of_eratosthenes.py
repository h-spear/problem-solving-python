# https://www.acmicpc.net/problem/2960

n, k = map(int, input().split())
prime = [True] * (n + 1)
prime[0] = False
prime[1] = False

cnt = 0
for i in range(2, n + 1):
    if not prime[i]:
        continue

    cnt += 1
    j = 2
    if cnt == k:
        print(i)
        break

    while i * j < n + 1:
        if prime[i * j]:
            prime[i * j] = False
            cnt += 1

        if cnt == k:
            print(i * j)
            exit(0)

        j += 1
