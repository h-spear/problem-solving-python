# https://www.acmicpc.net/problem/15565

n, k = map(int, input().split())
a = list(map(int, input().split()))

i = 0
j = 1
cnt = int(a[0] == 1)
INF = 1234567
answer = INF
while j < n:
    if cnt < k:
        if a[j] == 1:
            cnt += 1
        j += 1
    elif cnt > k:
        if a[i] == 1:
            cnt -= 1
        i += 1
    else:
        if i == j:
            print(1)
            exit(0)

        answer = min(answer, j - i)
        if a[i] == 1:
            cnt -= 1
        i += 1


while cnt == k and i != j:
    answer = min(answer, j - i)
    if a[i] == 1:
        cnt -= 1
    i += 1

if answer == INF:
    print(-1)
else:
    print(answer)
