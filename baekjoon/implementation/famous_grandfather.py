# https://www.acmicpc.net/problem/5766

from collections import defaultdict, Counter

while 1:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    hash = defaultdict(int)
    for _ in range(n):
        reward = list(map(int, input().split()))
        for x in reward:
            hash[x] += 1

    counter = Counter(hash)
    second_score = counter.most_common(2)[1][1]
    result = []
    for i, count in counter.items():
        if count == second_score:
            result.append(i)

    result.sort()
    for x in result:
        print(x, end=" ")
    print()
