# https://leetcode.com/problems/binary-tree-right-side-view/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict, deque


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        nodes = defaultdict(list)
        q = deque([(0, root)])
        max_lv = 0
        while q:
            lv, node = q.popleft()
            max_lv = max(max_lv, lv)

            nodes[lv].append(node.val)

            if node.left:
                q.append((lv + 1, node.left))
            if node.right:
                q.append((lv + 1, node.right))

        answer = [0] * (max_lv + 1)
        for lv in range(max_lv + 1):
            answer[lv] = nodes[lv][-1]
        return answer
