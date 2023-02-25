# https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right:
            return True
        elif not root.left or not root.right:
            return False

        q1 = deque()
        q2 = deque()
        q1.append(root.left)
        q2.append(root.right)
        while q1 and q2:
            x = q1.popleft()
            y = q2.popleft()

            if not x and not y:
                continue
            elif not x or not y:
                return False

            if x.val != y.val:
                return False

            if x.left:
                q1.append(x.left)
            else:
                q1.append(None)

            if x.right:
                q1.append(x.right)
            else:
                q1.append(None)

            if y.right:
                q2.append(y.right)
            else:
                q2.append(None)

            if y.left:
                q2.append(y.left)
            else:
                q2.append(None)

        return True
