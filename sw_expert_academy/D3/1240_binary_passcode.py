# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV15FZuqAL4CFAYD&categoryId=AV15FZuqAL4CFAYD&categoryType=CODE&problemTitle=1%EC%9D%BC%EC%B0%A8&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=1

# import sys
# sys.stdin = open("input.txt", "r")

gHash = {
    "0001101": 0,
    "0011001": 1,
    "0010011": 2,
    "0111101": 3,
    "0100011": 4,
    "0110001": 5,
    "0101111": 6,
    "0111011": 7,
    "0110111": 8,
    "0001011": 9,
}

T = int(input())
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n, m = map(int, input().split())
    barcode = ""
    for _ in range(n):
        input_string = input()
        if not barcode and "1" in input_string:
            barcode = input_string

    for i in range(m - 1, -1, -1):
        if barcode[i] == "1":
            barcode = barcode[i - 55 : i + 1]
            break

    # judge
    odd = 0
    even = 0
    for i in range(0, 56, 7):
        b = barcode[i : i + 7]
        if i // 7 in [0, 2, 4, 6]:
            odd += gHash[b]
        else:
            even += gHash[b]

    if (odd * 3 + even) % 10 == 0:
        print("#%d %d" % (test_case, odd + even))
    else:
        print("#%d %d" % (test_case, 0))

    # ///////////////////////////////////////////////////////////////////////////////////
