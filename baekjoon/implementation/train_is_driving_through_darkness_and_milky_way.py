# https://www.acmicpc.net/problem/15787

n, m = map(int, input().split())

trains = [0] * n

full = (1 << 20) - 1

for _ in range(m):
    line = list(map(int, input().split()))
    c = line[0]
    i = line[1] - 1
    if c == 1:
        x = line[2] - 1
        trains[i] |= 1 << x
    elif c == 2:
        x = line[2] - 1
        trains[i] &= ~(1 << x)
    elif c == 3:
        trains[i] <<= 1
    elif c == 4:
        trains[i] >>= 1
    trains[i] &= full

print(len(set(trains)))
