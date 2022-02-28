class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BST:
    def __init__(self, value):
        self.root = TreeNode(value)

    def insert(self, value):
        node = self.root
        while 1:
            if value < node.value:
                if node.left != None:
                    node = node.left
                else:
                    node.left = TreeNode(value)
                    break
            else:
                if node.right != None:
                    node = node.right
                else:
                    node.right = TreeNode(value)
                    break

    def search(self, value):
        node = self.root
        while node:
            if node.value == value:
                return True
            elif node.value > value:
                node = node.left
            else:
                node = node.right
        return False
