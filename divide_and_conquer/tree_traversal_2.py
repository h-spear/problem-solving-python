# https://www.acmicpc.net/problem/2263
# https://www.youtube.com/watch?v=18ncLrRKGiM


class TreeNode:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right


def find_idx(arr, idx, item):
    while True:
        if arr[idx] == item:
            return idx
        idx += 1


def fn(inorder, postorder, i_start, p_start, size):
    if size <= 0:
        return None
    root = postorder[p_start + size - 1]
    root_idx = find_idx(inorder, i_start, root)
    left_size = root_idx - i_start
    right_size = size - left_size - 1
    left = fn(inorder, postorder, i_start, p_start, left_size)
    right = fn(inorder, postorder, root_idx + 1, p_start + left_size, right_size)
    return TreeNode(root, left, right)


def preorder_print(tree):
    if tree == None:
        return
    print(tree.value, end=" ")
    preorder_print(tree.left)
    preorder_print(tree.right)


n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
tree = fn(inorder, postorder, 0, 0, n)
preorder_print(tree)
print("")
