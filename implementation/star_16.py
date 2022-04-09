# https://www.acmicpc.net/problem/10991

n = int(input())


def draw(i):
    for _ in range(i - 1):
        print("* ", end="")
    print("*")


for i in range(1, n + 1):
    print(" " * (n - i), end="")
    draw(i)
