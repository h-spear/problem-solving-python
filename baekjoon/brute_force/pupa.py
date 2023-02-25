# https://www.acmicpc.net/problem/15721

a = int(input())
t = int(input())
s = int(input())

pupa = [0] * 10001

turn = 0
cnt = 1
while turn <= 10000:
    for i in [0, 1, 0, 1]:
        if turn > 10000:
            break
        pupa[turn] = i
        turn += 1

    turn += cnt + 1

    j = 0
    while j <= cnt:
        if turn > 10000:
            break
        pupa[turn] = 1
        turn += 1
        j += 1
    cnt += 1

who = 0
cnt = 0
for x in pupa:
    if x == s:
        cnt += 1
    if cnt == t:
        print(who)
        break
    who = (who + 1) % a
