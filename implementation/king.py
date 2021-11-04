# https://www.acmicpc.net/problem/1063

pos1, pos2, n = input().split()
king = (ord(pos1[0]) - ord("A"), int(pos1[1]) - 1)
stone = (ord(pos2[0]) - ord("A"), int(pos2[1]) - 1)

# R L B T RT LT RB LB
dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, -1, 1, 1, 1, -1, -1]

command = {"R": 0, "L": 1, "B": 2, "T": 3, "RT": 4, "LT": 5, "RB": 6, "LB": 7}
for _ in range(int(n)):
    cmd = input()
    i = command[cmd]

    x, y = king
    nx = x + dx[i]
    ny = y + dy[i]

    if nx < 0 or nx >= 8 or ny < 0 or ny >= 8:
        continue

    if stone == (nx, ny):
        ############# 여기서 실수
        if nx + dx[i] < 0 or nx + dx[i] >= 8 or ny + dy[i] < 0 or ny + dy[i] >= 8:
            continue
        stone = (nx + dx[i], ny + dy[i])

    king = (nx, ny)

print(chr(king[0] + 65), king[1] + 1, sep="")
print(chr(stone[0] + 65), stone[1] + 1, sep="")
