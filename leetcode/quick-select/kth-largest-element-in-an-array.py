# https://leetcode.com/problems/kth-largest-element-in-an-array/

# quick select O(n) [worst case : O(n^2)]
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quick_select(left, right, idx):
            j = left
            pivot = nums[right]

            for i in range(left, right):
                if nums[i] <= pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    j += 1

            nums[j], nums[right] = nums[right], nums[j]

            if j > idx:
                return quick_select(left, j - 1, idx)
            elif j < idx:
                return quick_select(j + 1, right, idx)
            else:
                return nums[j]

        return quick_select(0, len(nums) - 1, len(nums) - k)


# heap O(nlogn)
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        ans = 0
        for num in nums:
            heapq.heappush(heap, (-num, num))

        for _ in range(k):
            ans = heapq.heappop(heap)[1]

        return ans
