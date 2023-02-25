# https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        parent = {}
        q = deque([root])
        start_node = None
        while q:
            x = q.popleft()
            if x.val == start:
                start_node = x

            if x.left:
                q.append(x.left)
                parent[x.left] = x
            if x.right:
                q.append(x.right)
                parent[x.right] = x

        q = deque([start_node])
        answer = -1
        visited = set()
        visited.add(start_node)
        while q:
            answer += 1
            for _ in range(len(q)):
                x = q.popleft()

                if x.left and x.left not in visited:
                    q.append(x.left)
                    visited.add(x.left)
                if x.right and x.right not in visited:
                    q.append(x.right)
                    visited.add(x.right)
                if x in parent and parent[x] not in visited:
                    q.append(parent[x])
                    visited.add(parent[x])

        return answer
