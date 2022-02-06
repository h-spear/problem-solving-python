# https://leetcode.com/problems/group-anagrams/
# TIP: sorted()는 문자열도 정렬하지만 리스트 형태로 return

from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = defaultdict(list)
        for str in strs:
            anagrams["".join(sorted(str))].append(str)

        return list(anagrams.values())


answer = Solution()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(answer.groupAnagrams(strs))
