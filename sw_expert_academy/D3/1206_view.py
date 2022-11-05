# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&passFilterYn=Y&contestProbId=AV134DPqAA8CFAYh&categoryId=AV134DPqAA8CFAYh&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=P&pageSize=10&pageIndex=1

# import sys
# sys.stdin = open("input.txt", "r")

T = 10
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////

    N = int(input())
    heights = list(map(int, input().split()))
    answer = 0

    for i, h in enumerate(heights):
        temp = 0
        for j in [-2, -1, 1, 2]:
            if i + j < 0 or i + j >= N:
                continue

            temp = max(temp, heights[i + j])

        if h - temp > 0:
            answer += h - temp

    print("#%d %d" % (test_case, answer))
    # ///////////////////////////////////////////////////////////////////////////////////
