# https://www.acmicpc.net/problem/10995

n = int(input())
pattern = "* " * (n - 1) + "*"
for i in range(n):
    if i & 1 == 0:
        print(pattern)
    else:
        print(" " + pattern)
