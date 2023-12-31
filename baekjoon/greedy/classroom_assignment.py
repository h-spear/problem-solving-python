# https://www.acmicpc.net/problem/11000

import sys
import heapq

input = lambda: sys.stdin.readline().rstrip()


def main():
    n = int(input())
    classes = []
    for _ in range(n):
        classes.append(tuple(map(int, input().split())))
    classes.sort(key=lambda x: x[0])

    heap = []
    for s, t in classes:
        if heap and heap[0][0] <= s:
            heapq.heappop(heap)
        heapq.heappush(heap, (t, s))

    print(len(heap))


if __name__ == "__main__":
    main()
