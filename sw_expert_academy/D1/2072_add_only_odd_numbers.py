# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&passFilterYn=Y&contestProbId=AV5QSEhaA5sDFAUq&categoryId=AV5QSEhaA5sDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=P&pageSize=10&pageIndex=1

# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////

    input_list = list(map(int, input().split()))
    summation = sum([num for num in input_list if num & 1])

    print("#%d %d" % (test_case, summation))

    # ///////////////////////////////////////////////////////////////////////////////////
