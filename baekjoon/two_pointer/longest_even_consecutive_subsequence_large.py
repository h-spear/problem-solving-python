# https://www.acmicpc.net/problem/22862

import sys

input = lambda: sys.stdin.readline().rstrip()


def main():
    N, K = map(int, input().split())
    S = list(map(int, input().split()))
    left = 0
    odd_cnt = 0
    answer = 0
    for right in range(0, N):
        if S[right] & 1:
            odd_cnt += 1

        while odd_cnt > K:
            odd_cnt -= S[left] & 1
            left += 1

        answer = max(answer, right - left - odd_cnt + 1)

    print(answer)


if __name__ == "__main__":
    main()
