# https://www.acmicpc.net/problem/2607

from collections import Counter

n = int(input())
f = input()
lf = len(f)
f_counter = Counter(f)
answer = 0

for _ in range(n - 1):
    word = input()
    c_counter = Counter(word)

    a = f_counter & c_counter
    if sum((f_counter - a).values()) <= 1 and sum((c_counter - a).values()) <= 1:
        answer += 1

print(answer)
