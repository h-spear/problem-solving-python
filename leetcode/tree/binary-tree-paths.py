# https://leetcode.com/problems/binary-tree-paths/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        answer = []
        path = []

        def traversal(node):
            if not node.left and not node.right:
                ss = ""
                for v in path:
                    ss += str(v)
                    ss += "->"
                answer.append(ss[:-2])
                return

            if node.left:
                path.append(node.left.val)
                traversal(node.left)
                path.pop()

            if node.right:
                path.append(node.right.val)
                traversal(node.right)
                path.pop()

        path.append(root.val)
        traversal(root)
        return answer
