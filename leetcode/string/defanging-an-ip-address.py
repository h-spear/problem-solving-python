# https://leetcode.com/problems/defanging-an-ip-address/

import re


class Solution:
    def defangIPaddr(self, address: str) -> str:
        return re.sub("\.", "[.]", address)
