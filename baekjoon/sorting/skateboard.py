# https://www.acmicpc.net/problem/28417

import sys

input = lambda: sys.stdin.readline().rstrip()


def main():
    n = int(input())

    answer = -1
    for _ in range(n):
        r1, r2, *t = map(int, input().split())
        t.sort()
        score = max(r1, r2) + t[3] + t[4]
        answer = max(answer, score)

    print(answer)


if __name__ == "__main__":
    main()
