# https://www.acmicpc.net/problem/7662

import heapq, sys

input = sys.stdin.readline


class DoubleHeap:
    def __init__(self):
        self.max_heap = []
        self.min_heap = []
        self.bag = dict()

    def length(self):
        return len(self.bag)

    def double_heappush(self, x):
        heapq.heappush(self.max_heap, (-x, x))
        heapq.heappush(self.min_heap, x)
        if x in self.bag.keys():
            self.bag[x] += 1
        else:
            self.bag[x] = 1

    def double_heappop(self, kind):
        # 가장 작은 원소
        if kind == -1:
            while True:
                if len(self.bag) == 0:
                    break
                removed = heapq.heappop(self.min_heap)
                if removed in self.bag.keys():
                    self.bag[removed] -= 1
                    if self.bag[removed] == 0:
                        self.bag.pop(removed)
                    break

        # 가장 큰 원소
        if kind == 1:
            while True:
                if len(self.bag) == 0:
                    break
                removed = heapq.heappop(self.max_heap)[1]
                if removed in self.bag.keys():
                    self.bag[removed] -= 1
                    if self.bag[removed] == 0:
                        self.bag.pop(removed)
                    break

    def double_heappeek(self, kind):
        # 가장 작은 원소
        if kind == -1:
            while True:
                if len(self.bag) == 0:
                    break
                removed = heapq.heappop(self.min_heap)
                if removed in self.bag.keys():
                    return removed

        # 가장 큰 원소
        if kind == 1:
            while True:
                if len(self.bag) == 0:
                    break
                removed = heapq.heappop(self.max_heap)[1]
                if removed in self.bag.keys():
                    return removed


for tc in range(int(input().rstrip())):
    n = int(input())
    heap = DoubleHeap()
    for _ in range(n):
        cmd, x = input().rstrip().split()
        if cmd == "I":
            heap.double_heappush(int(x))
        else:
            heap.double_heappop(int(x))

    if heap.length() == 0:
        print("EMPTY")
    else:
        print(heap.double_heappeek(1), heap.double_heappeek(-1))
