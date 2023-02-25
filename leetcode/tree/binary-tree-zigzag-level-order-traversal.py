# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict, deque


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        nodes = defaultdict(list)
        q = deque([(0, root)])
        max_lv = 0
        while q:
            lv, node = q.popleft()
            nodes[lv].append(node.val)
            max_lv = max(max_lv, lv)

            if node.left:
                q.append((lv + 1, node.left))
            if node.right:
                q.append((lv + 1, node.right))

        answer = [[] for _ in range(max_lv + 1)]
        for i in range(max_lv + 1):
            if i & 1:
                answer[i] = reversed(nodes[i])
            else:
                answer[i] = nodes[i]

        return answer
