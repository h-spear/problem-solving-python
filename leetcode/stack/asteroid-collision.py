# https://leetcode.com/problems/asteroid-collision/


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            stack.append(asteroid)

            while len(stack) >= 2:
                if (stack[-1] * stack[-2] > 0) or (stack[-1] > 0 and stack[-2] < 0):
                    break

                one = stack.pop()
                two = stack.pop()

                if one == -two:
                    continue
                elif abs(one) > abs(two):
                    stack.append(one)
                else:
                    stack.append(two)

        return stack
