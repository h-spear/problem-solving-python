# https://www.acmicpc.net/problem/2018

n = int(input())
i = 1
j = 1
curr = 1

answer = 0
while j <= n:
    if curr == n:
        answer += 1
        curr -= i
        i += 1
    elif curr > n:
        curr -= i
        i += 1
    else:
        j += 1
        curr += j

print(answer)
