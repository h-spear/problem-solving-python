# https://leetcode.com/problems/binary-trees-with-factors/


class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        counter = dict()
        n = len(arr)
        s = set(arr)
        p = int(1e9) + 7
        arr.sort()
        for i in range(n):
            num = arr[i]
            counter[num] = 1
            for j in range(i):
                divisor = arr[j]
                remainder = num % divisor
                quotient = num // divisor
                if remainder == 0 and quotient in s:
                    counter[num] += counter[divisor] * counter[quotient]
                    counter[num] %= p

        return sum(counter.values()) % p
