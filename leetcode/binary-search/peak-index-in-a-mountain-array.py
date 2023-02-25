# https://leetcode.com/problems/peak-index-in-a-mountain-array/


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        left = 0
        right = n - 1

        while left <= right:
            mid = (left + right) // 2

            if mid == 0:
                return mid + 1
            elif mid == n - 1:
                return mid - 1

            if arr[mid - 1] < arr[mid] and arr[mid] > arr[mid + 1]:
                return mid
            elif arr[mid - 1] < arr[mid]:
                left = mid + 1
            else:
                right = mid - 1

        return -1


# https://leetcode.com/problems/peak-index-in-a-mountain-array/discuss/2292517/Python-or-Binary-Search
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1

        while left <= right:
            mid = left + (right - left) // 2
            print(left, mid, right)
            if (
                arr[mid] > arr[mid + 1]
            ):  # Decesding order found, so we move towards left direction
                right = mid - 1
            else:
                left = mid + 1
        return left
