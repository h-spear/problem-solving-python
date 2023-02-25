# https://leetcode.com/problems/clone-graph/

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: "Node") -> "Node":
        save = dict()

        def make_clone(node):
            clone_node = Node(node.val, [])
            save[node.val] = clone_node
            for next_node in node.neighbors:
                if next_node.val in save:
                    clone_node.neighbors.append(save[next_node.val])
                else:
                    clone_node.neighbors.append(make_clone(next_node))

            return clone_node

        if not node:
            return None
        return make_clone(node)
