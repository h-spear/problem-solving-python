# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AYEXgKnKKg0DFARx&categoryId=AYEXgKnKKg0DFARx&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=1

# import sys
# sys.stdin = open("input.txt", "r")

line1 = ".#" * 50
line2 = "#." * 50
matrix = []
for _ in range(26):
    matrix.append(line1)
    matrix.append(line2)


def check(graph, n, m, s):
    for i in range(n):
        for j in range(m):
            if graph[i][j] == "?":
                continue
            if graph[i][j] != matrix[i + s][j]:
                return False
    return True


T = int(input())
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////

    n, m = map(int, input().split())
    graph = []
    for _ in range(n):
        graph.append(input())

    if check(graph, n, m, 0) or check(graph, n, m, 1):
        print(f"#{test_case} possible")
    else:
        print(f"#{test_case} impossible")

    # ///////////////////////////////////////////////////////////////////////////////////
