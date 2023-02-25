# https://leetcode.com/problems/open-the-lock/

from collections import deque


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1

        deadends = set(deadends)
        _hash = {str(i): [str((i - 1) % 10), str((i + 1) % 10)] for i in range(10)}
        q = deque(["0000"])
        visited = set(["0000"])
        count = -1
        while q:
            count += 1
            for _ in range(len(q)):
                pwd = q.popleft()

                if pwd == target:
                    return count

                for i in range(4):
                    for new in _hash[pwd[i]]:
                        new_pwd = pwd[:i] + new + pwd[i + 1 :]

                        if new_pwd in visited:
                            continue
                        if new_pwd in deadends:
                            continue

                        visited.add(new_pwd)
                        q.append(new_pwd)

        return -1
