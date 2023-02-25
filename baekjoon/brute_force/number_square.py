# https://www.acmicpc.net/problem/1051

n, m = map(int, input().split())
array = []
for _ in range(n):
    array.append(list(map(int, list(input()))))

answer = 0
for i in range(n):
    for j in range(m):
        for k in range(j, m):
            if array[i][j] != array[i][k]:
                continue
            length = k - j

            if i + length >= n:
                continue

            if array[i + length][j] == array[i + length][k] == array[i][j]:
                answer = max(answer, (length + 1) ** 2)

print(answer)
