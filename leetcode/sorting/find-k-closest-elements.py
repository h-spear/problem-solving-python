# https://leetcode.com/problems/find-k-closest-elements/


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        temp = []
        for i, num in enumerate(arr):
            temp.append((abs(num - x), i, num))
        temp.sort()

        answer = []
        for _, _, num in temp[:k]:
            answer.append(num)
        answer.sort()

        return answer
