# https://www.acmicpc.net/problem/1789

s = int(input())

now = 0
i = 1
while 1:
    now += i
    if now > s:
        break
    i += 1


print(i - 1)
