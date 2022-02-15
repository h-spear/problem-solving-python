# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def bfs(root: TreeNode):
            max_depth = 0

            q = deque([(1, root)])
            while q:
                depth, x = q.popleft()
                if x == None:
                    continue
                max_depth = max(max_depth, depth)

                q.append((depth + 1, x.left))
                q.append((depth + 1, x.right))
            return max_depth

        return bfs(root)


# 두 번째 코드
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        q = deque([root])
        depth = 0
        while q:
            depth += 1
            for _ in range(len(q)):
                x = q.popleft()

                if x.left:
                    q.append(x.left)
                if x.right:
                    q.append(x.right)

        return depth
