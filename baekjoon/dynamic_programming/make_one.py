x = int(input())

array = [30001] * (x + 1)
array[x] = 0

for i in range(x, 0, -1):
    num = array[i]
    if i % 5 == 0:
        array[i // 5] = min(array[i // 5], array[i] + 1)
    if i % 3 == 0:
        array[i // 3] = min(array[i // 3], array[i] + 1)
    if i % 2 == 0:
        array[i // 2] = min(array[i // 2], array[i] + 1)

    array[i - 1] = min(array[i - 1], array[i] + 1)

print(array[1])
