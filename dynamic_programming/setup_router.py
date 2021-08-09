# https://www.acmicpc.net/problem/2110


n, c = map(int, input().split())
houses = []

for _ in range(n):
    houses.append(int(input()))
houses.sort()

start = 1
end = houses[-1] - houses[0]
result = 0

# simulation
while start <= end:
    mid = (start + end) // 2
    value = houses[0]
    count = 1

    for i in range(1, n):
        if houses[i] >= value + mid:
            value = houses[i]
            count += 1

    if count >= c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)
