# https://www.acmicpc.net/problem/2138

import sys

input = lambda: sys.stdin.readline().rstrip()
INF = 987654321


def switch_push(switches, n, index):
    if index > 0:
        switches[index - 1] = 1 - switches[index - 1]
    switches[index] = 1 - switches[index]
    if index < n - 1:
        switches[index + 1] = 1 - switches[index + 1]


def test(original, target, n):
    res = 0
    cloned = [x for x in original]
    for i in range(n - 1):
        if cloned[i] != target[i]:
            res += 1
            switch_push(cloned, n, i + 1)

    for i in range(n):
        if cloned[i] != target[i]:
            return INF
    return res


def main():
    n = int(input())

    original = list(map(int, list(input())))
    target = list(map(int, list(input())))

    first = test(original, target, n)

    switch_push(original, n, 0)
    second = test(original, target, n)

    answer = min(first, second + 1)
    print(-1 if answer == INF else answer)


if __name__ == "__main__":
    main()
