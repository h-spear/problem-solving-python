# https://school.programmers.co.kr/learn/courses/30/lessons/150366

SIZE = 50
CELL_COUNT = SIZE * SIZE
EMPTY = "EMPTY"

table = None
parent = None


def get_indices(r, c):
    return (r - 1) * SIZE + c


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def change_value(idx, value):
    find_idx = find(idx)
    for i in range(CELL_COUNT + 1):
        if find(i) == find_idx:
            table[i] = value


def change_all_values(old, new):
    for i in range(CELL_COUNT + 1):
        if table[i] == old:
            table[i] = new


def merge(idx1, idx2):
    union(idx1, idx2)

    if table[idx1] != EMPTY:
        change_value(idx1, table[idx1])
    elif table[idx2] != EMPTY:
        change_value(idx1, table[idx2])


def unmerge(idx):
    find_idx = find(idx)
    checker = [False] * (CELL_COUNT + 1)

    for i in range(CELL_COUNT + 1):
        if find(i) == find_idx:
            checker[i] = True

    for i in range(CELL_COUNT + 1):
        if not checker[i]:
            continue

        parent[i] = i
        if i != idx:
            table[i] = EMPTY


def solution(commands):
    global table, parent
    table = [EMPTY] * (CELL_COUNT + 1)
    parent = [i for i in range(CELL_COUNT + 1)]
    answer = []

    for command in commands:
        cmd, *param = command.split()
        if cmd == "UPDATE":
            if len(param) == 3:
                r, c, value = param
                r, c = int(r), int(c)
                change_value(get_indices(r, c), value)
            else:
                change_all_values(*param)
        elif cmd == "MERGE":
            r1, c1, r2, c2 = map(int, param)
            merge(get_indices(r1, c1), get_indices(r2, c2))
        elif cmd == "UNMERGE":
            r, c = map(int, param)
            unmerge(get_indices(r, c))
        elif cmd == "PRINT":
            r, c = map(int, param)
            answer.append(table[get_indices(r, c)])

    return answer
