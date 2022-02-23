# https://programmers.co.kr/learn/courses/30/lessons/68936


def solution(arr):
    def quad_comp(arr, x, y, n):
        if n == 1:
            return [1 - arr[x][y], arr[x][y]]

        zero = 0
        one = 0
        topleft = quad_comp(arr, x, y, n // 2)
        bottomleft = quad_comp(arr, x + n // 2, y, n // 2)
        topright = quad_comp(arr, x, y + n // 2, n // 2)
        bottomright = quad_comp(arr, x + n // 2, y + n // 2, n // 2)
        for z, o in [topleft, bottomleft, topright, bottomright]:
            zero += z
            one += o

        if zero == 0:
            one = 1
        elif one == 0:
            zero = 1
        return [zero, one]

    return quad_comp(arr, 0, 0, len(arr))
