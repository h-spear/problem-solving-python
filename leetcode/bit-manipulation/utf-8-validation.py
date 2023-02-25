# https://leetcode.com/problems/utf-8-validation/


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        def get_first_one(num):
            cnt = 0
            for i in range(7, -1, -1):
                if num & 1 << i:
                    cnt += 1
                else:
                    break
            return cnt

        def check(num):
            if not (num & 1 << 7):
                return False
            if num & 1 << 6:
                return False
            return True

        i = 0
        while i < len(data):
            num = data[i]
            prefix_cnt = get_first_one(num)
            if prefix_cnt == 0:
                i += 1
            elif 2 <= prefix_cnt <= 4:
                prefix_cnt -= 1
                if i + prefix_cnt >= len(data):
                    return False
                for j in range(i + 1, i + prefix_cnt + 1):
                    if not check(data[j]):
                        return False
                i += prefix_cnt + 1
            else:
                return False

        return True
