# https://www.acmicpc.net/problem/2480

from collections import defaultdict

dice = defaultdict(int)
input_data = list(map(int, input().split()))

for x in input_data:
    dice[x] += 1

answer = 0
if len(dice) == 1:
    answer += 10000
    for x in dice:
        if dice[x] == 3:
            answer += x * 1000
elif len(dice) == 2:
    answer += 1000
    for x in dice:
        if dice[x] == 2:
            answer += x * 100
else:
    MAX = 0
    for x in dice:
        MAX = max(MAX, x)
    answer += MAX * 100

print(answer)
