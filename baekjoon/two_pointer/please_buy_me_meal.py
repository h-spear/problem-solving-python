# https://www.acmicpc.net/problem/31869

import sys

input = lambda: sys.stdin.readline().rstrip()


def solve():
    arr = [-1] * 88
    N = int(input())

    student = {}
    for _ in range(N):
        _input = input().split()
        S = _input[0]
        W = int(_input[1])
        D = int(_input[2])
        P = int(_input[3])
        student[S] = (W * 7 + D, P)

    money = {}
    for _ in range(N):
        _input = input().split()
        S = _input[0]
        M = int(_input[1])
        money[S] = M

    for name in student.keys():
        day, pay = student[name]
        if pay <= money[name]:
            arr[day] = pay

    answer = 0
    left = 0
    for right in range(88):
        if arr[right] > -1:
            answer = max(answer, right - left)
        else:
            left = right
            count = 0

    print(answer)


if __name__ == "__main__":
    solve()
