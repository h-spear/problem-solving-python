# https://www.acmicpc.net/problem/2980

n, l = map(int, input().split())

time = 0
now = 0
for _ in range(n):
    d, r, g = map(int, input().split())
    time += d - now
    t = time % (r + g)

    if t <= r:
        time += r - t + 1
    else:
        time += 1
    now = d + 1

print(time + l - now)
