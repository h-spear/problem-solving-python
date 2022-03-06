# https://www.acmicpc.net/problem/2491

n = int(input())
array = list(map(int, input().split()))
down = [1] * n
up = [1] * n

for i in range(1, n):
    if array[i - 1] <= array[i]:
        up[i] = up[i - 1] + 1

    if array[i - 1] >= array[i]:
        down[i] = down[i - 1] + 1

print(max(max(up), max(down)))
