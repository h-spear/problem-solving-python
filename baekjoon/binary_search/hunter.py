# https://www.acmicpc.net/problem/8983


def binary_search(a, b):
    left = 0
    right = m - 1
    while left <= right:
        mid = (left + right) // 2
        x = li[mid]
        distance = abs(x - a) + b

        if distance <= l:
            return True

        if x > a:
            right = mid - 1
        else:
            left = mid + 1
    return False


m, n, l = map(int, input().split())
li = list(map(int, input().split()))
animals = []
for _ in range(n):
    animals.append(tuple(map(int, input().split())))

li.sort()

answer = 0
for animal in animals:
    a, b = animal
    answer += int(binary_search(a, b))

print(answer)
