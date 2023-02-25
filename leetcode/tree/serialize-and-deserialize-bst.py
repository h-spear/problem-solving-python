# https://leetcode.com/problems/serialize-and-deserialize-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string."""

        if not root:
            return ""

        q = deque([root])
        result = []
        while q:
            x = q.popleft()

            if x:
                q.append(x.left)
                q.append(x.right)
                result.append(str(x.val))
            else:
                result.append("null")

        return " ".join(result)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree."""
        if not data:
            return None

        nums = deque(data.split(" "))
        root = TreeNode(nums.popleft())
        q = deque([root])
        while q:
            x = q.popleft()

            if nums:
                left = nums.popleft()
                x.left = TreeNode(left)
                if left != "null":
                    q.append(x.left)
            if nums:
                right = nums.popleft()
                x.right = TreeNode(right)
                if right != "null":
                    q.append(x.right)

        return root


# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
