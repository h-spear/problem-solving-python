# https://www.acmicpc.net/problem/20922

from collections import defaultdict

n, k = map(int, input().split())
a = list(map(int, input().split()))
hash = defaultdict(int)
i = 0
j = 1
hash[a[0]] += 1
answer = 1

while j < n:
    if hash[a[j]] < k:
        hash[a[j]] += 1
        j += 1
    elif hash[a[j]] >= k:
        hash[a[i]] -= 1
        i += 1

    answer = max(answer, j - i)

print(answer)
