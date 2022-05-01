# https://www.acmicpc.net/problem/1484

g = int(input())
i = 1
j = 1
answer = []
curr = 1
while i <= j:
    diff = j ** 2 - i ** 2
    if diff == g:
        answer.append(j)
        i += 1
    elif diff > g:
        i += 1
    else:
        j += 1

    if i > g and diff == 0:
        break

if answer:
    for x in answer:
        print(x)
else:
    print(-1)
