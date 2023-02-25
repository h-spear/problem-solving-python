# https://www.acmicpc.net/problem/2446

n = int(input())

for i in range(n):
    print(" " * i + "*" * (n - i - 1) + "*" * (n - i))

for i in range(n - 2, -1, -1):
    print(" " * i + "*" * (n - i - 1) + "*" * (n - i))
