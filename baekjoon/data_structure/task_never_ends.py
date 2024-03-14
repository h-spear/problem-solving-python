# https://www.acmicpc.net/problem/17952

import sys

input = lambda: sys.stdin.readline().rstrip()


def main():
    stack = []

    N = int(input())
    answer = 0
    for _ in range(N):
        x = list(map(int, input().split()))
        if x[0] == 1:
            A = x[1]
            T = x[2]
            stack.append([A, T])

        if len(stack) > 0:
            stack[-1][1] -= 1
            if stack[-1][1] == 0:
                answer += stack.pop()[0]

    print(answer)


if __name__ == "__main__":
    main()
