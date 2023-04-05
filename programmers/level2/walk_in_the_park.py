# https://school.programmers.co.kr/learn/courses/30/lessons/172928


def solution(park, routes):
    park = [list(parkStr) for parkStr in park]
    x, y = 0, 0
    n = len(park)
    m = len(park[0])

    direction_mapper = {"N": 0, "E": 1, "S": 2, "W": 3}
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    # 초기 로봇 위치
    for i in range(n):
        for j in range(m):
            if park[i][j] == "S":
                park[i][j] = "O"
                x = i
                y = j

    # 명령 수행
    for route in routes:
        direction, distance = route.split()
        direction = direction_mapper[direction]
        distance = int(distance)

        nx = x + distance * dx[direction]
        ny = y + distance * dy[direction]
        # 영역을 나가는지 체크
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue

        # 중간에 장애물이 있는지 체크
        obstacle = False
        for i in range(1, distance + 1):
            if park[x + i * dx[direction]][y + i * dy[direction]] == "X":
                obstacle = True
        if obstacle:
            continue

        # 여기까지 넘어오면 명령 수행
        x, y = nx, ny

    return [x, y]
