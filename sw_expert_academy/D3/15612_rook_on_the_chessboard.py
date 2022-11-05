# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AYOBfxwaAXsDFATW&categoryId=AYOBfxwaAXsDFATW&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=1

# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////

    graph = []
    rook_count = 0
    answer = True
    for _ in range(8):
        input_list = list(input())
        graph.append(input_list)
        rook_count_row = input_list.count("O")
        if answer and rook_count_row >= 2:
            answer = False
        rook_count += rook_count_row

    print(f"#{test_case} ", end="")
    if rook_count != 8 or not answer:
        print("no")
        continue

    for j in range(8):
        temp = 0
        for i in range(8):
            if graph[i][j] == "O":
                temp += 1
        if temp >= 2:
            answer = False

    if not answer:
        print("no")
        continue

    print("yes")

    # ///////////////////////////////////////////////////////////////////////////////////
