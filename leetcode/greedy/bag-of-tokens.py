# https://leetcode.com/problems/bag-of-tokens/

from collections import deque


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        answer = 0
        score = 0
        tokens.sort()
        tokens = deque(tokens)
        while tokens:
            least = tokens[0]
            if least <= power:
                tokens.popleft()
                power -= least
                score += 1
            elif score >= 1:
                power += tokens.pop()
                score -= 1
            else:
                break

            answer = max(answer, score)

        return answer
