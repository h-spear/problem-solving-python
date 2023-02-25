# https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/


class Solution:
    def average(self, salary: List[int]) -> float:
        minn = 1234567
        maxx = -1
        summ = 0
        count = 0

        for s in salary:
            minn = min(minn, s)
            maxx = max(maxx, s)

        for s in salary:
            if s == minn or s == maxx:
                continue
            summ += s
            count += 1

        return summ / count
