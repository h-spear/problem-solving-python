# https://school.programmers.co.kr/learn/courses/30/lessons/42892

import sys
from collections import defaultdict
from bisect import bisect_left

sys.setrecursionlimit(10 ** 6)


def solution(nodeinfo):
    node_count = len(nodeinfo)
    tree = [dict() for _ in range(node_count + 1)]
    nodes_by_lv = defaultdict(list)
    map_y_to_lv = dict()
    map_num_to_x = dict()
    ys = sorted(set([y for x, y in nodeinfo]), reverse=True)
    for i, y in enumerate(ys):
        map_y_to_lv[y] = i + 1

    for num, (x, y) in enumerate(nodeinfo):
        lv = map_y_to_lv[y]
        nodes_by_lv[lv].append((x, num + 1))
        map_num_to_x[num + 1] = x

    for lv in nodes_by_lv:
        nodes_by_lv[lv].sort()

    def preorder(tree, x, result):
        result.append(x)
        if "left" in tree[x]:
            preorder(tree, tree[x]["left"], result)
        if "right" in tree[x]:
            preorder(tree, tree[x]["right"], result)

    def postorder(tree, x, result):
        if "left" in tree[x]:
            postorder(tree, tree[x]["left"], result)
        if "right" in tree[x]:
            postorder(tree, tree[x]["right"], result)
        result.append(x)

    def dfs(lv, num, left, right):
        x = map_num_to_x[num]
        if lv + 1 not in nodes_by_lv:
            return

        candidates = nodes_by_lv[lv + 1]
        lc = len(candidates)
        idx = bisect_left(candidates, (x, 0))
        right_child = candidates[idx] if idx < lc else None
        left_child = candidates[idx - 1] if idx > 0 else None

        if left_child and left_child[0] > left:
            tree[num]["left"] = left_child[1]
            dfs(lv + 1, left_child[1], left, x)
        if right_child and right_child[0] < right:
            tree[num]["right"] = right_child[1]
            dfs(lv + 1, right_child[1], x, right)

    root = nodes_by_lv[1][0][1]
    dfs(1, root, -1, 100001)

    preorder_result = []
    postorder_result = []
    preorder(tree, root, preorder_result)
    postorder(tree, root, postorder_result)

    return [preorder_result, postorder_result]
