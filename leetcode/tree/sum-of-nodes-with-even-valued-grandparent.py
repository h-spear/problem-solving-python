# https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict, deque


class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def get_grandparent(node):
            parent = parent_hash[node]
            grandparent = parent_hash[parent]
            return grandparent

        parent_hash = defaultdict(TreeNode)
        q = deque([(0, root)])
        while q:
            lv, node = q.popleft()

            if node.left:
                parent_hash[node.left] = node
                q.append((lv + 1, node.left))
            if node.right:
                parent_hash[node.right] = node
                q.append((lv + 1, node.right))

        q = deque([(0, root)])
        answer = 0
        while q:
            lv, node = q.popleft()

            if lv >= 2:
                grandparent = get_grandparent(node)
                if grandparent.val & 1 == 0:
                    answer += node.val

            if node.left:
                q.append((lv + 1, node.left))
            if node.right:
                q.append((lv + 1, node.right))

        return answer
