# https://www.acmicpc.net/problem/1969

from collections import defaultdict
from collections import Counter

n, m = map(int, input().split())
dna = []
for _ in range(n):
    dna.append(list(input()))

answer = ""
distance = 0
for i in range(m):
    _dict = defaultdict(int)
    for j in range(n):
        _dict[dna[j][i]] += 1

    counter = sorted(
        Counter(_dict).most_common(4),
        key=lambda x: (x[1], -ord(x[0])),
        reverse=True,
    )
    answer += counter[0][0]
    for idx, val in enumerate(counter):
        if idx == 0:
            continue
        distance += val[1]

print(answer)
print(distance)
