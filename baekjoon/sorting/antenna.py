# https://www.acmicpc.net/problem/18310
# 중간 값이 최소!

n = int(input())
houses = list(map(int, input().split()))
houses.sort()
print(houses[n // 2 - 1])
