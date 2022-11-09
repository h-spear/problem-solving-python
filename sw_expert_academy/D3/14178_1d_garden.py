# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AX_N3oSqcyUDFARi&categoryId=AX_N3oSqcyUDFARi&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=1

# import sys
# sys.stdin = open("input.txt", "r")


import math

T = int(input())
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n, d = map(int, input().split())

    print(f"#{test_case} {math.ceil(n / (2* d + 1))}")
    # ///////////////////////////////////////////////////////////////////////////////////
