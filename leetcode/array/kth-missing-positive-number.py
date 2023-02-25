# https://leetcode.com/problems/kth-missing-positive-number/

# O(n)
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        s = set(arr)
        i = 1
        while 1:
            if i in s:
                pass
            else:
                k -= 1

            if k == 0:
                return i

            i += 1

        return -1
