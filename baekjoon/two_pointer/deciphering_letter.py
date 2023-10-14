# https://www.acmicpc.net/problem/1593

from collections import defaultdict


def check():
    for key in wCounterKeys:
        if wCounter[key] != sCounter[key]:
            return False

    return True


g, n = map(int, input().split())
W = input()
S = input()

wCounter = defaultdict(int)
wCounterKeys = wCounter.keys()
sCounter = defaultdict(int)
for c in W:
    wCounter[c] += 1

left = 0
right = g
for i in range(g):
    sCounter[S[i]] += 1

answer = 0

if check():
    answer += 1

while right < n:
    sCounter[S[right]] += 1
    sCounter[S[left]] -= 1
    left += 1
    right += 1
    if check():
        answer += 1

print(answer)
