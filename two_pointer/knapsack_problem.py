# https://www.acmicpc.net/problem/1450
# meet in the middle algorithm
# 참고 : https://ca.ramel.be/100

from itertools import combinations
from bisect import bisect_right

n, c = map(int, input().split())
weights = list(map(int, input().split()))

weights_a = weights[: len(weights) // 2]
weights_b = weights[len(weights) // 2 :]

weight_sum_a = []
weight_sum_b = []


def func(source, target):
    for i in range(len(source) + 1):
        for x in combinations(source, i):
            target.append(sum(x))


func(weights_a, weight_sum_a)
func(weights_b, weight_sum_b)
weight_sum_b.sort()

answer = 0
for i in range(len(weight_sum_a)):
    now = weight_sum_a[i]
    answer += bisect_right(weight_sum_b, c - now)

print(answer)
