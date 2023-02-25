# https://leetcode.com/problems/maximum-width-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        answer = 0
        q = deque([(0, root)])

        while q:
            answer = max(answer, q[-1][0] - q[0][0] + 1)
            nq = deque()
            while q:
                i, node = q.popleft()
                if node.left:
                    nq.append((2 * i, node.left))
                if node.right:
                    nq.append((2 * i + 1, node.right))
            q = nq
        return answer
