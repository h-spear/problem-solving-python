# https://leetcode.com/problems/maximum-number-of-removable-characters/
# Runtime: 2209 ms, faster than 99.71% of Python3 online submissions for Maximum Number of Removable Characters.


class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def check(k):
            remover = set(removable[:k])
            j = 0
            for i in range(ls):
                if i in remover:
                    continue

                if s[i] == p[j]:
                    j += 1
                    if j == lp:
                        return True

            return False

        ls = len(s)
        lp = len(p)
        left = 0
        right = len(removable)
        answer = 0

        while left <= right:
            mid = (left + right) // 2

            if check(mid):
                left = mid + 1
                answer = mid
            else:
                right = mid - 1
        return answer
