# https://www.acmicpc.net/problem/10867

n = int(input())
a = list(map(int, input().split()))
a = list(set(a))
a.sort()
print(*a)
