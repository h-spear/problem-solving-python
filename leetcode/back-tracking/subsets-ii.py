# https://leetcode.com/problems/subsets-ii/


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        s = set()
        path = []
        n = len(nums)

        def dfs(idx):
            copied = path[::]
            copied.sort()
            s.add(tuple(copied))

            for i in range(idx, n):
                path.append(nums[i])
                dfs(i + 1)
                path.pop()

        dfs(0)
        answer = []
        for candidate in s:
            answer.append(list(candidate))

        return answer
