# https://www.acmicpc.net/problem/1991


class TreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self):
        self.root = None

    def preorder(self, node):
        if node == None:
            return
        print(node.data, end="")
        self.preorder(node.left)
        self.preorder(node.right)

    def postorder(self, node):
        if node == None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.data, end="")

    def inorder(self, node):
        if node == None:
            return
        self.inorder(node.left)
        print(node.data, end="")
        self.inorder(node.right)


hash = {x: TreeNode(x) for x in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}
tree = BinaryTree()
tree.root = hash["A"]
n = int(input())
for _ in range(n):
    a, b, c = input().split()

    if b != ".":
        hash[a].left = hash[b]
    if c != ".":
        hash[a].right = hash[c]

tree.preorder(tree.root)
print()
tree.inorder(tree.root)
print()
tree.postorder(tree.root)
