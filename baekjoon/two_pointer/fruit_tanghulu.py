# https://www.acmicpc.net/problem/30804

import sys

input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    S = list(map(int, input().split()))
    counter = [0] * 10

    kind = 0
    low = 0
    answer = 0
    for high in range(0, N):
        counter[S[high]] += 1
        if counter[S[high]] == 1:
            kind += 1

        while kind > 2:
            counter[S[low]] -= 1
            if counter[S[low]] == 0:
                kind -= 1
            low += 1

        answer = max(answer, high - low + 1)

    print(answer)


if __name__ == "__main__":
    main()
