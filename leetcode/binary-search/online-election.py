# https://leetcode.com/problems/online-election/

from bisect import bisect_left
from collections import defaultdict


class TopVotedCandidate:
    def __init__(self, persons: List[int], times: List[int]):
        counter = defaultdict(int)
        n = len(persons)
        winner_by_t = [0] * n
        winner = -1
        max_vote = 0
        for i in range(n):
            counter[persons[i]] += 1
            if counter[persons[i]] >= max_vote:
                max_vote = counter[persons[i]]
                winner = persons[i]
            winner_by_t[i] = winner

        self.winner_by_t = winner_by_t
        self.times = times

    def q(self, t: int) -> int:
        idx = bisect_left(self.times, (t + 0.5)) - 1
        return self.winner_by_t[idx]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
