# https://www.acmicpc.net/problem/10819

from itertools import permutations

n = int(input())
a = list(map(int, input().split()))

answer = 0


def func(li):
    global answer
    temp = 0
    for i in range(n - 1):
        temp += abs(li[i + 1] - li[i])
    answer = max(answer, temp)


for candidate in permutations(a, n):
    func(candidate)

print(answer)
