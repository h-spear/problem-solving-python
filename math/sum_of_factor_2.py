# https://www.acmicpc.net/problem/17427

n = int(input())
mem = [1] * (n + 1)
mem[0] = 0

for i in range(2, n + 1):
    for j in range(i, n + 1, i):
        if j % i == 0:
            mem[j] += i

print(sum(mem))
