# https://www.acmicpc.net/problem/5639

import sys

sys.setrecursionlimit(10 ** 5)


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root == None:
            self.root = TreeNode(value)
            return

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

    def postorder(self, node):
        if node == None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.value)


input = lambda: sys.stdin.readline().rstrip()
tree = BST()
while 1:
    try:
        value = int(input())
    except:
        break
    tree.insert(value)

tree.postorder(tree.root)
