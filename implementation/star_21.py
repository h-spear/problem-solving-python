# https://www.acmicpc.net/problem/10996


def draw(star, col):
    global n
    if col == n:
        print("")
        return
    if star:
        print("*", end="")
    else:
        print(" ", end="")
    draw(1 - star, col + 1)


n = int(input())
if n == 1:
    print("*")
    exit()

for i in range(n):
    draw(1, 0)
    draw(0, 0)
