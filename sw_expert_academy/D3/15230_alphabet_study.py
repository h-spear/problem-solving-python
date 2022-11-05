# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AYLnMQT6vPADFATf&categoryId=AYLnMQT6vPADFATf&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=1

# import sys
# sys.stdin = open("input.txt", "r")

alphabet = "abcdefghijklmnopqrstuvwxyz"
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////

    count = 0
    input_string = input()
    for a, b in zip(alphabet, input_string):
        if a == b:
            count += 1
        else:
            break

    print(f"{test_case} {count}")

    # ///////////////////////////////////////////////////////////////////////////////////
