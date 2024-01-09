# https://www.acmicpc.net/problem/20920

import sys
from collections import defaultdict

input = lambda: sys.stdin.readline().rstrip()


def main():
    N, M = map(int, input().split())
    counter = defaultdict(int)
    for _ in range(N):
        word = input()
        if len(word) < M:
            continue
        counter[word] += 1

    lst = list(counter.items())
    lst.sort(key=lambda x: (-x[1], -len(x[0]), x[0]))

    for word, _ in lst:
        print(word)


if __name__ == "__main__":
    main()
