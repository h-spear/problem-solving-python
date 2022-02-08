# https://leetcode.com/problems/jewels-and-stones/submissions/

from collections import defaultdict, Counter


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        hash = defaultdict(int)
        for stone in stones:
            hash[stone] += 1

        answer = 0
        for jewel in jewels:
            answer += hash[jewel]
        return answer


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        answer = 0
        # Counter로 만들면 자동으로 dict
        hash = Counter(stones)
        for jewel in jewels:
            answer += hash[jewel]
        return answer


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(stone in jewels for stone in stones)
