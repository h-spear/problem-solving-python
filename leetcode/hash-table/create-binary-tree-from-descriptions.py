# https://leetcode.com/problems/create-binary-tree-from-descriptions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        hashmap = {}
        parents = set()
        childs = set()
        for p, c, _ in descriptions:
            parents.add(p)
            childs.add(c)

        root = list(parents - childs)[0]

        for p, c, isL in descriptions:
            if p not in hashmap:
                hashmap[p] = TreeNode(p)
            if c not in hashmap:
                hashmap[c] = TreeNode(c)

            p_node = hashmap[p]
            c_node = hashmap[c]

            if isL:
                p_node.left = c_node
            else:
                p_node.right = c_node

        return hashmap[root]
