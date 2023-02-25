# https://leetcode.com/problems/time-based-key-value-store/

from collections import defaultdict
from bisect import bisect_right


class TimeMap:
    def __init__(self):
        self.hashMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if not self.hashMap[key]:
            return ""
        idx = bisect_right(self.hashMap[key], (timestamp + 0.5, ""))
        if idx == 0:
            return ""
        return self.hashMap[key][idx - 1][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
