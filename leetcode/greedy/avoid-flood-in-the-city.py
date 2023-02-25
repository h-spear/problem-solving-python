# https://leetcode.com/problems/avoid-flood-in-the-city/


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        s = set()
        result = [-1] * len(rains)
        last = {}
        zeros = []
        for i, rain in enumerate(rains):
            if rain == 0:
                zeros.append(i)
            elif rain not in s:
                s.add(rain)
                last[rain] = i
            else:
                idx = -1
                for j in range(len(zeros)):
                    if zeros[j] > last[rain]:
                        idx = zeros.pop(j)
                        break

                if idx == -1:
                    return []

                result[idx] = rain
                last[rain] = i

        o = max(rains)
        while zeros:
            idx = zeros.pop()
            result[idx] = o

        return result
