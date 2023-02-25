# https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Solution:
    def getTargetCopy(
        self, original: TreeNode, cloned: TreeNode, target: TreeNode
    ) -> TreeNode:
        q = deque([(original, cloned)])

        while q:
            onode, cnode = q.popleft()

            if onode == target:
                return cnode

            if onode.left:
                q.append((onode.left, cnode.left))
            if onode.right:
                q.append((onode.right, cnode.right))

        return None
