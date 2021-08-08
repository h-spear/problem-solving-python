n = int(input())
direction = input().split()

x = 1
y = 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ["L", "R", "U", "D"]

for cmd in direction:
    for i in range(len(move_types)):
        if cmd == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue

    x, y = nx, ny

print(x, y)
