# https://leetcode.com/problems/valid-palindrome/


class Solution:
    def isPalindrome(self, s: str) -> bool:
        array = []
        for i in s.upper():
            if i.isalnum():
                array.append(i)

        length = len(array)
        for i in range(length // 2):
            if array[i] != array[length - i - 1]:
                return False

        return True


answer = Solution()
print(answer.isPalindrome("race a car"))
