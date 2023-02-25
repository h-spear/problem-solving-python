# https://www.acmicpc.net/problem/1251

from itertools import combinations

s = input()
ls = len(s)
candidate = []
for i, j in combinations(range(1, ls), 2):
    seg1 = s[:i][::-1]
    seg2 = s[i:j][::-1]
    seg3 = s[j:][::-1]
    temp = seg1 + seg2 + seg3
    candidate.append(temp)

candidate.sort()
print(candidate[0])
