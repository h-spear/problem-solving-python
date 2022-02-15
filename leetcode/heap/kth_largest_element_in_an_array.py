# https://leetcode.com/problems/kth-largest-element-in-an-array/

import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        answer = 0
        for num in nums:
            heapq.heappush(heap, (-num, num))

        for _ in range(k):
            answer = heapq.heappop(heap)
        return answer[1]
