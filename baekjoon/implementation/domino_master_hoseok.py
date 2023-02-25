# https://www.acmicpc.net/problem/20165

n, m, r = map(int, input().split())
graph = []
attack = []
defense = []
score = 0
state = [["S"] * m for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
dir = {"E": 0, "W": 1, "S": 2, "N": 3}

for _ in range(n):
    graph.append(list(map(int, input().split())))

for _ in range(r):
    x, y, d = input().split()
    attack.append((int(x) - 1, int(y) - 1, dir[d]))
    x, y = map(int, input().split())
    defense.append((x - 1, y - 1))


def push_domino(x, y, d):
    global score
    if x < 0 or y < 0 or x >= n or y >= m:
        return
    if state[x][y] == "F":
        return

    k = graph[x][y]
    state[x][y] = "F"
    score += 1
    for _ in range(k - 1):
        x += dx[d]
        y += dy[d]
        push_domino(x, y, d)


def build_domino(x, y):
    state[x][y] = "S"


def simulation():
    for round in range(r):
        push_domino(*attack[round])
        build_domino(*defense[round])


def show():
    print(score)
    for x in state:
        print(*x)


simulation()
show()
