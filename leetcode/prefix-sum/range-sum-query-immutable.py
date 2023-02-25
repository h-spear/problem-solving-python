# https://leetcode.com/problems/range-sum-query-immutable/


class NumArray:
    def __init__(self, nums: List[int]):
        n = len(nums)
        p_sum = [nums[0]]
        for i in range(1, n):
            p_sum.append(nums[i] + p_sum[-1])
        p_sum.append(0)

        self.p_sum = p_sum

    def sumRange(self, left: int, right: int) -> int:
        return self.p_sum[right] - self.p_sum[left - 1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
