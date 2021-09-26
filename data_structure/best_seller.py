# https://www.acmicpc.net/problem/1302

from collections import defaultdict

n = int(input())
dict = defaultdict(int)

for _ in range(n):
    book = input()
    dict[book] += 1

most = max(dict.values())
best_seller = []
for key in dict:
    if dict[key] == most:
        best_seller.append(key)

best_seller.sort()
print(best_seller[0])
