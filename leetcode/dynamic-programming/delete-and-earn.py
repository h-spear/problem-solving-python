# https://leetcode.com/problems/delete-and-earn/


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        _hash = dict()

        for num in nums:
            if num not in _hash:
                _hash[num] = num
            else:
                _hash[num] += num

        arr = list(sorted(_hash.items()))
        n = len(arr)
        dp = [0] * (n + 10)
        dp[0] = arr[0][1]

        for i in range(1, n):
            if arr[i][0] - 1 == arr[i - 1][0]:
                dp[i] = max(dp[i - 2] + arr[i][1], dp[i - 1])
            else:
                dp[i] = dp[i - 1] + arr[i][1]

        return dp[n - 1]
