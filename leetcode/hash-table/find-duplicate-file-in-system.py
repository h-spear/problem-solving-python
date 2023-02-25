# https://leetcode.com/problems/find-duplicate-file-in-system/

import re
from collections import defaultdict


class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for path in paths:
            fragment = path.split()
            directory = fragment[0]
            for i in range(1, len(fragment)):
                file_content = re.search("\(.+\)", fragment[i])[0]
                filename = fragment[i][0 : fragment[i].index("(")]
                hashmap[file_content].append(directory + "/" + filename)

        return [v for v in hashmap.values() if len(v) >= 2]
