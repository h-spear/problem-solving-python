# https://leetcode.com/problems/snapshot-array/

from collections import defaultdict


class SnapshotArray:
    def __init__(self, length: int):
        self.hash_map = {0: defaultdict(int)}
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        self.hash_map[self.snap_id][index] = val

    def snap(self) -> int:
        self.hash_map[self.snap_id + 1] = self.hash_map[self.snap_id].copy()
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        return self.hash_map[snap_id][index]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
