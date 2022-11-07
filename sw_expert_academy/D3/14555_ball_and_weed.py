# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AYGtoa3qARcDFARC&categoryId=AYGtoa3qARcDFARC&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=1

# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////

    input_string = input()
    for pattern in ["()", "(|", "|)"]:
        input_string = input_string.replace(pattern, "!")

    print(f"#{test_case} {input_string.count('!')}")

    # ///////////////////////////////////////////////////////////////////////////////////
