from collections import deque
from copy import deepcopy
from itertools import permutations


def value_of_array(A):
    res = INF
    for r in A:
        res = min(sum(r), res)
    return res


def rotate(A, r, c, _s):
    temp = deque()
    for s in range(1, _s + 1):
        for j in range(c - s, c + s + 1):
            temp.append(A[r - s][j])

        for i in range(r - s + 1, r + s + 1):
            temp.append(A[i][c + s])

        for j in range(c + s - 1, c - s - 1, -1):
            temp.append(A[r + s][j])

        for i in range(r + s - 1, r - s, -1):
            temp.append(A[i][c - s])

        temp.appendleft(temp.pop())

        for j in range(c - s, c + s + 1):
            A[r - s][j] = temp.popleft()

        for i in range(r - s + 1, r + s + 1):
            A[i][c + s] = temp.popleft()

        for j in range(c + s - 1, c - s - 1, -1):
            A[r + s][j] = temp.popleft()

        for i in range(r + s - 1, r - s, -1):
            A[i][c - s] = temp.popleft()


if __name__ == "__main__":
    n, m, k = map(int, input().split())
    graph = []
    operations = []
    INF = 987654321
    answer = INF

    for _ in range(n):
        graph.append(list(map(int, input().split())))

    for _ in range(k):
        r, c, s = map(int, input().split())
        operations.append((r - 1, c - 1, s))

    for candidate in permutations(operations, k):
        A = deepcopy(graph)
        for r, c, s in candidate:
            rotate(A, r, c, s)

        answer = min(answer, value_of_array(A))

    print(answer)
