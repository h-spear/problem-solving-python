# https://leetcode.com/problems/find-original-array-from-doubled-array/

from collections import Counter


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) & 1:
            return []

        target_cnt = len(changed) // 2
        curr_cnt = 0
        counter = Counter(changed)
        changed.sort(reverse=True)
        answer = []

        for i in range(len(changed)):
            num = changed[i]
            if num == 0:
                if counter[0] >= 2:
                    curr_cnt += 1
                    counter[0] -= 2
                    answer.append(0)
            elif counter[num * 2]:
                curr_cnt += 1
                counter[num] -= 1
                counter[num * 2] -= 1
                answer.append(num)

        if curr_cnt != target_cnt:
            return []
        return answer
