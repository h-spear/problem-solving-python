def rotate_matrix_90(A):
    n = len(A)  # length of row
    m = len(A[0])  # length of column
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = A[i][j]
    return result


def rotate_matrix_180(A):
    n = len(A)  # length of row
    m = len(A[0])  # length of column
    result = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            result[n - i - 1][m - j - 1] = A[i][j]
    return result


def rotate_matrix_270(A):
    n = len(A)  # length of row
    m = len(A[0])  # length of column
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[m - j - 1][i] = A[i][j]
    return result


def print_array(A):
    for i in range(len(A)):
        for j in range(len(A[0])):
            print(A[i][j], end=" ")
        print()
    print()


array = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [0, 1, 2]]

print_array(array)
print_array(rotate_matrix_90(array))
print_array(rotate_matrix_180(array))
print_array(rotate_matrix_270(array))
