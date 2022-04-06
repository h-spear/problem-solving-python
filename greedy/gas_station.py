# https://www.acmicpc.net/problem/13305

n = int(input())
road = list(map(int, input().split()))
cost = list(map(int, input().split()))
answer = 0
i = 0
while i < n - 1:
    curr = cost[i]
    dist = road[i]
    j = i + 1
    while j < n - 1 and cost[j] > curr:
        dist += road[j]
        j += 1
    answer += curr * dist
    i = j

print(answer)
