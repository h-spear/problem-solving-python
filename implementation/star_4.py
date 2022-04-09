# https://www.acmicpc.net/problem/2441

n = int(input())
for i in range(n):
    print(" " * i + "*" * (n - i))
