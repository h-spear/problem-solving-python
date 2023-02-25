# https://leetcode.com/problems/copy-list-with-random-pointer/

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        dp = defaultdict(Node)

        # counter
        p = head
        count = 0
        while p:
            count += 1
            p = p.next

        # generate dummylist
        new = None
        while count:
            count -= 1
            new = Node(0, new)

        # set value
        p = head
        q = new
        while p:
            q.val = p.val
            q.random = p.random
            dp[p] = q

            p = p.next
            q = q.next

        # set random
        q = new
        while q:
            if q.random:
                q.random = dp[q.random]
            q = q.next

        return new
