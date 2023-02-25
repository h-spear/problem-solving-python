# https://leetcode.com/problems/fizz-buzz/


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = [str(i) for i in range(1, n + 1)]

        for i in range(14, n, 15):
            answer[i] = "FizzBuzz"

        for i in range(2, n, 3):
            if answer[i] != "FizzBuzz":
                answer[i] = "Fizz"

        for i in range(4, n, 5):
            if answer[i] != "FizzBuzz":
                answer[i] = "Buzz"

        return answer
