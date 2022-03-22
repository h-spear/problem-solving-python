# https://www.acmicpc.net/problem/21610

n, m = map(int, input().split())
graph = []
command = []
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
for _ in range(n):
    graph.append(list(map(int, input().split())))

for _ in range(m):
    command.append(list(map(int, input().split())))


def move_cloud_and_raining(cloud, d, s):
    for i in range(len(cloud)):
        x, y = cloud[i]
        nx = (x + s * dx[d]) % n
        ny = (y + s * dy[d]) % n
        cloud[i] = (nx, ny)
        graph[nx][ny] += 1


def water_copy_bug(cloud):
    for x, y in cloud:
        cnt = 0
        for i in [1, 3, 5, 7]:
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if graph[nx][ny] == 0:
                continue
            cnt += 1
        graph[x][y] += cnt


def generate_cloud(cloud):
    temp = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] < 2:
                continue
            if (i, j) in cloud:
                continue
            graph[i][j] -= 2
            temp.append((i, j))
    return temp


def rain_rain(command):
    cloud = [(n - 1, 0), (n - 1, 1), (n - 2, 0), (n - 2, 1)]

    for d, s in command:
        move_cloud_and_raining(cloud, d - 1, s)
        water_copy_bug(cloud)
        cloud = generate_cloud(cloud)

    answer = 0
    for x in graph:
        answer += sum(x)
    print(answer)


rain_rain(command)
