# https://www.acmicpc.net/problem/14659

n = int(input())
a = list(map(int, input().split()))

answer = 0
temp = a[0]
cnt = 0
for x in a:
    if x == temp:
        continue
    elif x > temp:
        temp = x
        answer = max(answer, cnt)
        cnt = 0
    else:
        cnt += 1
answer = max(answer, cnt)

print(answer)
