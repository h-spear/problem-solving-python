# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict, deque


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if k == 0:
            return [target.val]

        parent = defaultdict(TreeNode)
        parent[root] = None
        q = deque([root])
        while q:
            node = q.popleft()

            if node.left:
                parent[node.left] = node
                q.append(node.left)
            if node.right:
                parent[node.right] = node
                q.append(node.right)

        answer = []
        q = deque([(0, target)])
        visited = set()
        visited.add(target.val)
        while q:
            d, node = q.popleft()
            if d == k:
                answer.append(node.val)
                continue

            for nnode in [node.left, node.right, parent[node]]:
                if not nnode:
                    continue
                if nnode.val in visited:
                    continue
                visited.add(nnode.val)
                q.append((d + 1, nnode))

        return answer
