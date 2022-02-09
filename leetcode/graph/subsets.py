# https://leetcode.com/problems/subsets/


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []

        def dfs(path=[], idx=0):
            answer.append(path[:])
            # if len(path) == len(nums):
            #    return

            for i in range(idx, len(nums)):
                if nums[i] in path:
                    continue
                path.append(nums[i])
                dfs(path, i + 1)
                path.pop()

        dfs()
        return answer
