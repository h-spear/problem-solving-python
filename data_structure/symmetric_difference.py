# https://www.acmicpc.net/problem/1269

n, m = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))
print(len((b - a) | (a - b)))
