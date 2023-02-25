# https://www.acmicpc.net/problem/1449

n, l = map(int, input().split())
a = [0] * 1001
leak = list(map(int, input().split()))
for x in leak:
    a[x] = 1

i = 1
answer = 0
while i <= 1000:
    if a[i] == 1:
        i += l
        answer += 1
    else:
        i += 1

print(answer)
