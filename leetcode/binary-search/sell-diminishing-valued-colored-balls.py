# https://leetcode.com/problems/sell-diminishing-valued-colored-balls/

import heapq


class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        def f(x):
            res = 0
            for i in inventory:
                if (i - x) > 0:
                    res += i - x
            return res

        p = int(1e9) + 7
        n = len(inventory)
        answer = 0
        common = 0
        left = 1
        right = int(1e9)
        while left <= right:
            mid = (left + right) // 2
            if f(mid) <= orders:
                common = mid
                right = mid - 1
            else:
                left = mid + 1

        for i in range(n):
            x = inventory[i]
            if x - common > 0:
                answer += x * (x + 1) // 2 - common * (common + 1) // 2
                answer %= p
                orders -= x - common
                inventory[i] = common

        heap = []
        while inventory:
            heapq.heappush(heap, -inventory.pop())

        while orders:
            orders -= 1
            curr = -heapq.heappop(heap)
            answer += curr
            answer %= p
            if curr - 1 > 0:
                heapq.heappush(heap, -(curr - 1))

        return answer
