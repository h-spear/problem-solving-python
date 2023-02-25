# https://leetcode.com/problems/k-closest-points-to-origin/


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        answer = []
        indexer = []
        for i, point in enumerate(points):
            x, y = point
            dist = (x ** 2 + y ** 2) ** 0.5
            indexer.append((dist, i))

        indexer.sort()
        for i in range(k):
            _, idx = indexer[i]
            answer.append(points[idx])

        return answer
