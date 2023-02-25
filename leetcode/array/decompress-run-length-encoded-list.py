# https://leetcode.com/problems/decompress-run-length-encoded-list/


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        output = []
        length = len(nums)
        for i in range(0, length, 2):
            freq, val = nums[i], nums[i + 1]
            output += [val] * freq

        return output
