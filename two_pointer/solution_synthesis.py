# https://www.acmicpc.net/problem/14921

n = int(input())
a = list(map(int, input().split()))

i = 0
j = n - 1
a.sort()
answer = 223456789

while i < j:
    new = a[i] + a[j]
    if abs(answer) > abs(new):
        answer = new

    if new < 0:
        i += 1
    elif new > 0:
        j -= 1
    else:
        answer = 0
        break


print(answer)
