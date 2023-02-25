# https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        nodes = set()
        q = deque([root])
        root.val = 1
        nodes.add(0)
        while q:
            node = q.popleft()

            if node.left:
                node.left.val = 2 * node.val
                nodes.add(2 * node.val - 1)
                q.append(node.left)
            if node.right:
                node.right.val = 2 * node.val + 1
                nodes.add(2 * node.val)
                q.append(node.right)
        self.nodes = nodes

    def find(self, target: int) -> bool:
        return target in self.nodes


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
