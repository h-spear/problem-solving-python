# https://leetcode.com/problems/assign-cookies/


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        answer = 0
        g.sort(reverse=True)
        s.sort(reverse=True)

        while g and s:
            child = g.pop()

            while s:
                cookie = s.pop()
                if cookie >= child:
                    answer += 1
                    break

        return answer
