# https://leetcode.com/problems/generate-parentheses/


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []

        def dfs(i, curr, op):
            if i == n * 2:
                answer.append(curr)
                return

            cl = i - op

            if op <= n and cl < op:
                dfs(i + 1, curr + ")", op)

            if op < n:
                dfs(i + 1, curr + "(", op + 1)

        dfs(0, "", 0)
        return answer
