# https://www.acmicpc.net/problem/1181

import sys

words = [set() for _ in range(51)]
n = int(input())
for _ in range(n):
    word = sys.stdin.readline().rstrip()
    words[len(word)].add(word)

for i in range(1, 51):
    words[i] = list(words[i])
    words[i].sort()

for i in range(1, 51):
    for word in words[i]:
        print(word)
