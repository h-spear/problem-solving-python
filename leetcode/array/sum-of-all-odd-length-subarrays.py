# https://leetcode.com/problems/sum-of-all-odd-length-subarrays/


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:

        n = len(arr)
        answer = 0

        for length in range(1, n + 1, 2):
            curr = 0
            i = 0
            j = length
            for k in range(j):
                curr += arr[k]

            answer += curr

            while j < n:
                curr += arr[j]
                curr -= arr[i]
                i += 1
                j += 1
                answer += curr

        return answer
