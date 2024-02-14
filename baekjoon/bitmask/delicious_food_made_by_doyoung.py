# https://www.acmicpc.net/problem/2961

import sys

input = lambda: sys.stdin.readline().rstrip()

N = -1
S = []
B = []


def test(select_bit):
    t = [1, 0]
    for i in range(N):
        if (select_bit & (1 << i)) > 0:
            t[0] *= S[i]
            t[1] += B[i]

    return abs(t[0] - t[1])


def main():
    global N, S, B

    N = int(input())
    for _ in range(N):
        s, b = map(int, input().split())
        S.append(s)
        B.append(b)

    answer = 9876543210
    for b in range(1, (1 << N)):
        answer = min(answer, test(b))

    print(answer)


if __name__ == "__main__":
    main()
