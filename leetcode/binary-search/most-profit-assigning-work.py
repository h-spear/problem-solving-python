# https://leetcode.com/problems/most-profit-assigning-work/

from bisect import bisect_left


class Solution:
    def maxProfitAssignment(
        self, difficulty: List[int], profit: List[int], worker: List[int]
    ) -> int:
        n = len(difficulty)
        arr = []
        parr = []
        answer = 0

        for d, p in zip(difficulty, profit):
            arr.append((d, p))

        arr.sort()
        parr.append(arr[0][1])
        for i in range(1, n):
            parr.append(max(parr[-1], arr[i][1]))

        for w in worker:
            if w < arr[0][0]:
                continue
            find = (w + 0.5, 0)
            idx = min(bisect_left(arr, find) - 1, n - 1)
            answer += parr[idx]

        return answer
