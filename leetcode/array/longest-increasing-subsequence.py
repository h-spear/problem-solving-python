from bisect import bisect_left


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        length = 0
        q = []
        for x in nums:
            if not q:
                q.append(x)
                length += 1
                continue

            if q[-1] < x:
                q.append(x)
                length += 1
            else:
                idx = bisect_left(q, x)
                q[idx] = x

        return length
