# https://leetcode.com/problems/group-anagrams/

from collections import defaultdict

# 1
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)

        for _str in strs:
            key = tuple(sorted(_str))
            group[key].append(_str)

        return list(group.values())


# 2
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        tuples = []
        dict = defaultdict(list)
        for str in strs:
            tuples.append(("".join(sorted(str)), str))

        for data in tuples:
            dict[data[0]].append(data[1])

        return list(dict.values())
