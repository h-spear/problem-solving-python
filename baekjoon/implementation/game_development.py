n, m = map(int, input().split())
a, b, d = map(int, input().split())
field = []

for _ in range(0, m):
    row = list(map(int, input().split()))
    field.append(row)


def rotate_left(d):
    return (d + 3) % 4


def direction_back(d):
    return (d + 2) % 4


def isField(r, c):
    if r >= 0 and r <= n and c >= 0 and c <= m:
        return True
    return False


def move(r, c):
    global a, b
    a, b = r, c


def visited(r, c):
    field[r][c] = 2


# 북, 동, 남, 서
move_r = [-1, 0, 1, 0]
move_c = [0, 1, 0, -1]

visited(a, b)
rotate_count = 0
count = 1
while True:
    d = rotate_left(d)
    rotate_count += 1
    nr = a + move_r[d]
    nc = b + move_c[d]
    if isField(nr, nc):
        if field[nr][nc] == 0:
            a, b = nr, nc
            count += 1
            rotate_count = 0
            visited(a, b)
    if rotate_count == 4:
        back = direction_back(d)
        nr = a + move_r[back]
        nc = b + move_c[back]
        if isField(nr, nc):
            if field[nr][nc] == 1:
                break
            a = nr
            b = nc
            rotate_count = 0

print(count)
