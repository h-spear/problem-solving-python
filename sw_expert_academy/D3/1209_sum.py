# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV13_BWKACUCFAYh&categoryId=AV13_BWKACUCFAYh&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=1

# import sys
# sys.stdin = open("input.txt", "r")

for _ in range(10):
    # ///////////////////////////////////////////////////////////////////////////////////
    test_case = int(input())

    answer = 0
    matrix = []
    for _ in range(100):
        input_list = list(map(int, input().split()))
        matrix.append(input_list)
        answer = max(answer, sum(input_list))

    dtemp1 = 0
    dtemp2 = 0
    for j in range(100):
        temp = 0
        for i in range(100):
            temp += matrix[i][j]
        answer = max(answer, temp)

        dtemp1 += matrix[j][j]
        dtemp2 += matrix[j][100 - j - 1]

    answer = max(answer, dtemp1, dtemp2)
    print(f"#{test_case} {answer}")

    # ///////////////////////////////////////////////////////////////////////////////////
