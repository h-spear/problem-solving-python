# https://leetcode.com/problems/sort-characters-by-frequency/


class Solution:
    def frequencySort(self, s: str) -> str:
        answer = ""
        for char, cnt in sorted(Counter(s).items(), key=lambda x: (-x[1], x[0])):
            answer += char * cnt
        return answer
