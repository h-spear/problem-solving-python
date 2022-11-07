# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AYCnY9Kqu6YDFARx&categoryId=AYCnY9Kqu6YDFARx&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=1

from itertools import permutations

# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////

    n = input()
    now = int(n)
    for candidate in permutations(n, len(n)):
        new = int("".join(candidate))
        if new > now and new % now == 0:
            print(f"#{test_case} possible")
            break
    else:
        print(f"#{test_case} impossible")

    # ///////////////////////////////////////////////////////////////////////////////////
