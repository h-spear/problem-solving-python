# https://www.acmicpc.net/problem/1339
# 초반에 처리하지 못했던 상황 : https://www.acmicpc.net/board/view/85400

import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
words = []
for _ in range(n):
    word = input()
    words.append(word)

alphabet = {alpha: 0 for alpha in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}

for word in words:
    lw = len(word)
    for i, char in enumerate(word):
        bit = 10 ** (lw - i - 1)
        alphabet[char] += bit

li = []
for alpha, val in alphabet.items():
    li.append((val, alpha))

hash = dict()
li.sort(reverse=True)
num = 9

for i in range(10):
    char = li[i][1]
    hash[char] = str(num)
    num -= 1

nums = []
for word in words:
    num = ""
    for char in word:
        num += hash[char]

    nums.append(int(num))

print(sum(nums))
