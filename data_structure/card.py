# https://www.acmicpc.net/problem/11652

from collections import Counter


n = int(input())
cards = [int(input()) for _ in range(n)]
counter = Counter(cards)
answer = 2 ** 62
most_common = counter.most_common(1)[0][1]
for key in counter:
    if counter[key] == most_common:
        if answer > key:
            answer = key

print(answer)
