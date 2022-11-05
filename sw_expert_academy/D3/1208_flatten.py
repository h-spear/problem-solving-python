# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV139KOaABgCFAYh&categoryId=AV139KOaABgCFAYh&categoryType=CODE&problemTitle=1%EC%9D%BC%EC%B0%A8&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=1

# import sys
# sys.stdin = open("input.txt", "r")

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////

    dump = int(input())
    box = list(map(int, input().split()))
    for _ in range(dump):
        box.sort()
        box[-1] -= 1
        box[0] += 1

    box.sort()
    print("#%d %d" % (test_case, box[-1] - box[0]))

    # ///////////////////////////////////////////////////////////////////////////////////
