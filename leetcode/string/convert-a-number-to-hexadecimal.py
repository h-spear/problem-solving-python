# https://leetcode.com/problems/convert-a-number-to-hexadecimal/

import re


class Solution:
    def toHex(self, num: int) -> str:
        _hash = {
            "0000": "0",
            "0001": "1",
            "0010": "2",
            "0011": "3",
            "0100": "4",
            "0101": "5",
            "0110": "6",
            "0111": "7",
            "1000": "8",
            "1001": "9",
            "1010": "a",
            "1011": "b",
            "1100": "c",
            "1101": "d",
            "1110": "e",
            "1111": "f",
        }

        def num_to_bin(number):
            binary = ""
            while number:
                binary += str(number & 1)
                number >>= 1
            return binary[::-1].zfill(32)

        def bin_to_hex(binary):
            hexa = ""
            for i in range(0, 32, 4):
                hexa += _hash[binary[i : i + 4]]
            return hexa

        def rev(binary):
            converted = ""
            for i in range(32):
                if binary[i] == "1":
                    converted += "0"
                else:
                    converted += "1"
            return converted

        if num == 0:
            return "0"

        if num < 0:
            hexa = bin_to_hex(rev(num_to_bin(abs(num) - 1)))
        else:
            hexa = bin_to_hex(num_to_bin(num))

        return re.sub("^0+", "", hexa)
