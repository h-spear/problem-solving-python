# https://www.acmicpc.net/problem/2438

n = int(input())

for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()
