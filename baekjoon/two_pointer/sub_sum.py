# https://www.acmicpc.net/problem/1806

n, s = map(int, input().split())
arr = list(map(int, input().split()))

i = 0
j = 1
curr = arr[0]
answer = 123456
find = False
while i < j:
    if curr >= s:
        answer = min(answer, j - i)
        find = True
        curr -= arr[i]
        i += 1

    if j == n and curr < s:
        break
    elif curr < s:
        curr += arr[j]
        j += 1

if find:
    print(answer)
else:
    print(0)
