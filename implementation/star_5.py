# https://www.acmicpc.net/problem/2442

n = int(input())
for i in range(n - 1, -1, -1):
    print(" " * i + "*" * (n - i - 1) + "*" * (n - i))
