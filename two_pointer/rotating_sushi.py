# https://www.acmicpc.net/problem/2531
# https://www.acmicpc.net/problem/15961

from collections import defaultdict


n, d, k, c = map(int, input().split())
sushi = []
hash = defaultdict(int)
for _ in range(n):
    sushi.append(int(input()))

sushi += sushi[:k]

for i in range(k):
    hash[sushi[i]] += 1

n = len(sushi)
i = 0
j = k
answer = len(hash)
if c not in hash:
    answer += 1

while j < n:
    hash[sushi[j]] += 1
    j += 1

    hash[sushi[i]] -= 1
    if hash[sushi[i]] == 0:
        del hash[sushi[i]]
    i += 1

    now = len(hash) if c in hash else len(hash) + 1
    answer = max(answer, now)

print(answer)
