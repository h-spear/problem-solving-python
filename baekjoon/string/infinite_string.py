# https://www.acmicpc.net/problem/12871
# 최소 공배수만큼 곱하면 더 효율적임

s = input()
t = input()
ls, lt = len(s), len(t)
s = s * lt
t = t * ls

if s == t:
    print(1)
else:
    print(0)
