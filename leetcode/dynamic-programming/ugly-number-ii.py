# https://leetcode.com/problems/ugly-number-ii/

# dp
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        two = 1
        three = 1
        five = 1
        dp = [0] * (n + 1)
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = min(2 * dp[two], 3 * dp[three], 5 * dp[five])

            if dp[i] == 2 * dp[two]:
                two += 1
            if dp[i] == 3 * dp[three]:
                three += 1
            if dp[i] == 5 * dp[five]:
                five += 1

        return dp[n]


# heap
import heapq


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        visited = set([1])

        while len(visited) <= 2000:
            num = heapq.heappop(heap)

            if num * 2 not in visited:
                heapq.heappush(heap, num * 2)
                visited.add(num * 2)

            if num * 3 not in visited:
                heapq.heappush(heap, num * 3)
                visited.add(num * 3)

            if num * 5 not in visited:
                heapq.heappush(heap, num * 5)
                visited.add(num * 5)

        visited = list(visited)
        visited.sort()
        return visited[n - 1]
