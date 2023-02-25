# https://www.acmicpc.net/problem/19941

n, k = map(int, input().split())
p = list(input())
lp = len(p)
vs = [0] * lp

for i, char in enumerate(p):
    if char == "H":
        s = max(i - k, 0)
        e = min(i + k + 1, n)
        for j in range(s, e):
            if p[j] == "P" and not vs[j]:
                vs[j] = 1
                break


print(sum(vs))
