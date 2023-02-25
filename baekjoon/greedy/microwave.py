# https://www.acmicpc.net/problem/10162

btn = [300, 60, 10]
ans = [0, 0, 0]

time = int(input())

ans[0] += time // 300
time %= 300

ans[1] += time // 60
time %= 60

ans[2] += time // 10
time %= 10

if time != 0:
    print(-1)
else:
    for x in ans:
        print(x, end=" ")
