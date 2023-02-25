# https://leetcode.com/problems/decode-xored-array/


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        output = [first]
        for new in encoded:
            output.append(output[-1] ^ new)

        return output
