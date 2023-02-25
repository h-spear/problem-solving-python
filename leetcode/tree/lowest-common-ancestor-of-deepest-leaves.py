# https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict, deque


class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def get_lca(node1, node2):
            if depth[node1] > depth[node2]:
                node1, node2 = node2, node1

            while depth[node1] != depth[node2]:
                node2 = parent[node2]

            while node1 != node2:
                node1 = parent[node1]
                node2 = parent[node2]

            return node1

        depth = defaultdict(int)
        parent = defaultdict(TreeNode)
        nodes = defaultdict(list)
        q = deque([(0, root)])
        max_depth = 0

        while q:
            lv, node = q.popleft()
            depth[node] = lv
            max_depth = max(max_depth, lv)
            nodes[lv].append(node)

            if node.left:
                parent[node.left] = node
                q.append((lv + 1, node.left))
            if node.right:
                parent[node.right] = node
                q.append((lv + 1, node.right))

        if len(nodes[max_depth]) == 1:
            return nodes[max_depth][0]
        else:
            one = nodes[max_depth].pop()
            two = nodes[max_depth].pop()
            lca = get_lca(one, two)
            while nodes[max_depth]:
                node = nodes[max_depth].pop()
                lca = get_lca(lca, node)
            return lca
