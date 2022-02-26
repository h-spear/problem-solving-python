# https://www.acmicpc.net/problem/11478

s = input()

S = set()
i = 1
for i in range(len(s)):
    for j in range(i, len(s)):
        S.add(s[i : j + 1])

print(len(S))
