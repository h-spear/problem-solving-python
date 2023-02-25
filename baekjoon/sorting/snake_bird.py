# https://www.acmicpc.net/problem/16435

n, l = map(int, input().split())
h = list(map(int, input().split()))
h.sort(reverse=True)
while h and h[-1] <= l:
    h.pop()
    l += 1

print(l)
