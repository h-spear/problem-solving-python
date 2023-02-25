# https://www.acmicpc.net/problem/3273

n = int(input())
a = list(map(int, input().split()))
a.sort()
x = int(input())

i = 0
j = n - 1
cnt = 0
while i < j:
    if a[i] + a[j] > x:
        j -= 1
        continue

    if a[i] + a[j] < x:
        i += 1
        continue

    if a[i] + a[j] == x:
        cnt += 1

        if i + 1 >= n or j - 1 < 0:
            break

        if a[i] == a[i + 1]:
            i += 1
        else:
            j -= 1


print(cnt)
