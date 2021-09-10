# https://leetcode.com/problems/valid-palindrome/


class Solution:
    def isPalindrome(self, s: str) -> bool:
        array = []
        for i in s.upper():
            if i.isalnum():
                array.append(i)

        # array[::-1] -> 내부적으로 C로 구현되어 속도가 빠르다!
        return array == array[::-1]


answer = Solution()
print(answer.isPalindrome("race a car"))
