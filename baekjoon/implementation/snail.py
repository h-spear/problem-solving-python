# https://www.acmicpc.net/problem/1913


def draw_snail(n):
    global array
    x, y = n // 2, n // 2
    top, bottom, right, left = x - 1, x + 1, y + 1, y - 1
    i = 1
    while i <= n ** 2:
        while x > top:
            array[x][y] = i
            i += 1
            x -= 1
        top -= 1

        while y < right:
            array[x][y] = i
            i += 1
            y += 1
        right += 1

        while x < bottom:
            array[x][y] = i
            i += 1
            x += 1
        bottom += 1

        while y > left:
            array[x][y] = i
            i += 1
            y -= 1
        left -= 1


def print_array(n):
    global array
    for i in range(n):
        for j in range(n):
            print(array[i][j], end=" ")
        print()


def find_index(num, n):
    global array
    for i in range(n):
        for j in range(n):
            if array[i][j] != num:
                continue
            return i + 1, j + 1


n = int(input())
num = int(input())
array = [[0] * 1000 for _ in range(1000)]
draw_snail(n)
x, y = find_index(num, n)
print_array(n)
print(x, y)
