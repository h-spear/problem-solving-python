# https://leetcode.com/problems/permutations/


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []

        def dfs(path, i):
            if i == len(nums):
                answer.append(path)
                return

            for num in nums:
                if num in path:
                    continue
                _path = path.copy()
                # [:]로 copy할 수 있음
                # _path = path[:]
                _path.append(num)
                dfs(_path, i + 1)

        dfs([], 0)
        return answer
        # return list(permutations(nums, len(nums)))
