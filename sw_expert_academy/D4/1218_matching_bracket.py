# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=4&contestProbId=AV14eWb6AAkCFAYD&categoryId=AV14eWb6AAkCFAYD&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=ALL&select-1=4&pageSize=10&pageIndex=1

# import sys
# sys.stdin = open("input.txt", "r")

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n = int(input())
    string = input()
    stack = []
    pair = {"}": "{", "]": "[", ")": "(", ">": "<"}
    flag = True
    for char in string:
        if char in "({[<":
            stack.append(char)
        else:
            if not stack or pair[char] != stack.pop():
                flag = False
                break

    print(f"#{test_case} {int(flag)}")
    # ///////////////////////////////////////////////////////////////////////////////////
