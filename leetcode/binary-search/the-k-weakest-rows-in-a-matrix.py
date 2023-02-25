# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        candidate = []

        def get_soldier_count(row):
            left = 0
            right = n - 1
            while left <= right:
                mid = (left + right) // 2
                if row[mid] == 1:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        for i in range(m):
            count = get_soldier_count(mat[i])
            candidate.append((count, i))

        candidate.sort()
        return [idx for cnt, idx in candidate][:k]
