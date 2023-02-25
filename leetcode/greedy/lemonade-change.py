# https://leetcode.com/problems/lemonade-change/


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        counter = {5: 0, 10: 0, 20: 0}
        for bill in bills:
            if bill == 20:
                counter[20] += 1
                if counter[10] and counter[5]:
                    counter[10] -= 1
                    counter[5] -= 1
                elif counter[5] >= 3:
                    counter[5] -= 3
                else:
                    return False
            elif bill == 10:
                counter[10] += 1
                if counter[5]:
                    counter[5] -= 1
                else:
                    return False
            elif bill == 5:
                counter[5] += 1

        return True
