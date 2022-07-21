# https://www.acmicpc.net/problem/2110
# https://hongcoding.tistory.com/3

n, c = map(int, input().split())
x = [int(input()) for _ in range(n)]
x.sort()
lx = len(x)

start = 1
end = x[-1] - x[0]
answer = 0

while start <= end:
    cnt = 1
    old = x[0]
    mid = (start + end) // 2
    for i in range(1, lx):
        now = x[i]
        if now >= old + mid:
            cnt += 1
            old = now

    if cnt >= c:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)
