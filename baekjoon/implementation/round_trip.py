# https://www.acmicpc.net/problem/18311

n, k = map(int, input().split())
dist = [0]
input_data = list(map(int, input().split()))
dist.extend(input_data)
dist.extend(reversed(input_data))

run = 0
for i, x in enumerate(dist):
    if i == 0:
        continue

    run += x
    if run > k:
        if i <= n:
            print(i)
        else:
            print(2 * n - i + 1)
        break
