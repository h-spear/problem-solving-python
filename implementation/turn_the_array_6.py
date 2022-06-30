def flip_vertical(A):
    n = len(A)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[n - i - 1][j] = A[i][j]
    return result


def flip_horizontal(A):
    n = len(A)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[i][n - j - 1] = A[i][j]
    return result


def rotate_degree_90(A):
    n = len(A)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[j][n - i - 1] = A[i][j]
    return result


def rotate_degree_270(A):
    n = len(A)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[n - j - 1][i] = A[i][j]
    return result


def flip_vertical_subarray(A, l):
    h = hap[l]
    result = [[0] * n for _ in range(n)]
    for i in range(0, n, h):
        for j in range(0, n, h):

            for _i in range(h):
                for _j in range(h):
                    result[n - i - h + _i][j + _j] = A[i + _i][j + _j]
    return result


def flip_horizontal_subarray(A, l):
    h = hap[l]
    result = [[0] * n for _ in range(n)]
    for i in range(0, n, h):
        for j in range(0, n, h):

            for _i in range(h):
                for _j in range(h):
                    result[i + _i][n - j - h + _j] = A[i + _i][j + _j]
    return result


def rotate_90_subarray(A, l):
    h = hap[l]
    result = [[0] * n for _ in range(n)]
    for i in range(0, n, h):
        for j in range(0, n, h):

            for _i in range(h):
                for _j in range(h):
                    result[j + _i][n - i - h + _j] = A[i + _i][j + _j]
    return result


def rotate_270_subarray(A, l):
    h = hap[l]
    result = [[0] * n for _ in range(n)]
    for i in range(0, n, h):
        for j in range(0, n, h):

            for _i in range(h):
                for _j in range(h):
                    result[n - j - h + _i][i + _j] = A[i + _i][j + _j]
    return result


def operation(A, k, l):
    h = hap[l]
    if k <= 4:
        for i in range(0, n, h):
            for j in range(0, n, h):
                temp = [[0] * h for _ in range(h)]
                for _i in range(h):
                    for _j in range(h):
                        temp[_i][_j] = A[i + _i][j + _j]

                if k == 1:
                    temp = flip_vertical(temp)
                elif k == 2:
                    temp = flip_horizontal(temp)
                elif k == 3:
                    temp = rotate_degree_90(temp)
                elif k == 4:
                    temp = rotate_degree_270(temp)

                for _i in range(h):
                    for _j in range(h):
                        A[i + _i][j + _j] = temp[_i][_j]

        return A
    else:
        if k == 5:
            return flip_vertical_subarray(A, l)
        elif k == 6:
            return flip_horizontal_subarray(A, l)
        elif k == 7:
            return rotate_90_subarray(A, l)
        elif k == 8:
            return rotate_270_subarray(A, l)

    return None


def print_array(A):
    for x in A:
        print(*x)


if __name__ == "__main__":
    n, r = map(int, input().split())
    n = 2 ** n
    hap = {i: 2 ** i for i in range(10)}
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))

    ops = []
    for _ in range(r):
        ops.append(tuple(map(int, input().split())))

    for k, l in ops:
        graph = operation(graph, k, l)

    print_array(graph)
