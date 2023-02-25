# https://leetcode.com/problems/find-latest-group-of-size-m/


class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)

        if m == n:
            return n

        ranges = [0] * (n + 2)
        answer = -1
        for i, num in enumerate(arr):
            left = right = num

            if ranges[left - 1]:
                left = ranges[left - 1]
            if ranges[right + 1]:
                right = ranges[right + 1]
            ranges[left], ranges[right] = right, left

            if right - num == m or num - left == m:
                answer = i

        return answer


# 시간초과
class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        def find(parent, x):
            if parent[x] != x:
                parent[x] = find(parent, parent[x])
            return parent[x]

        def union(parent, a, b):
            a = find(parent, a)
            b = find(parent, b)
            if a < b:
                parent[b] = a
            else:
                parent[a] = b

        n = len(arr)
        answer = -1
        parent = [i for i in range(n + 1)]

        for step, num in enumerate(arr):
            union(parent, num, num - 1)
            i = n
            while i > 0:
                x = find(parent, i)
                if i - x == m:
                    answer = step + 1
                    break
                i = x - 1

        return answer
