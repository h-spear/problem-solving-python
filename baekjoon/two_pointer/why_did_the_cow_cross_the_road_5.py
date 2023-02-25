# https://www.acmicpc.net/problem/14465
# sliding window

n, k, b = map(int, input().split())
arr = [0] * n
for _ in range(b):
    num = int(input())
    arr[num - 1] = 1

i = 0
j = k - 1
now = sum(arr[0:k])
answer = now
while j < n - 1:
    now -= arr[i]
    i += 1
    j += 1
    now += arr[j]

    answer = min(answer, now)


print(answer)
