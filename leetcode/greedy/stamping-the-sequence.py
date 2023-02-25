# https://leetcode.com/problems/stamping-the-sequence/
# https://www.youtube.com/watch?v=J5XMEHw1HR0


class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        n = len(target)
        m = len(stamp)
        result = []

        move, max_moves = 0, 10 * n
        premove = 0

        def check(src, tar):
            flag = False
            for i in range(m):
                if src[i] == tar[i]:
                    flag = True
                elif src[i] == "?":
                    continue
                else:
                    return False
            return flag

        while move < max_moves:
            premove = move
            for i in range(n - m + 1):

                # check stamp == subsequence
                if check(target[i : i + m], stamp):
                    move += 1
                    result.append(i)
                    target = target[:i] + "?" * m + target[i + m :]
                    if target == "?" * n:
                        return reversed(result)

            if premove == move:
                return []
