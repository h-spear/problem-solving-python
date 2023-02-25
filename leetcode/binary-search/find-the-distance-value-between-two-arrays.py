# https://leetcode.com/problems/find-the-distance-value-between-two-arrays/


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        n = len(arr2)
        arr2.sort()
        cnt = 0
        for num in arr1:
            flag = True
            left = 0
            right = n - 1
            while left <= right:
                mid = (left + right) // 2

                if abs(num - arr2[mid]) <= d:
                    flag = False
                    break
                elif arr2[mid] > num:
                    right = mid - 1
                else:
                    left = mid + 1

            if flag:
                cnt += 1

        return cnt
