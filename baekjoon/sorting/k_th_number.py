# https://www.acmicpc.net/problem/11004

n, k = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
print(a[k - 1])
