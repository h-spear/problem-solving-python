# https://www.acmicpc.net/problem/2822

li = []
for i in range(8):
    li.append((int(input()), i))

li.sort(reverse=True)
idx = []
summation = 0

for i in range(5):
    score, _idx = li[i]
    summation += score
    idx.append(_idx + 1)

idx.sort()

print(summation)
print(*idx)
