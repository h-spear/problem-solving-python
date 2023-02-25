# https://www.acmicpc.net/problem/19583

s, e, q = input().split()

before = set()
after = set()
while 1:
    try:
        t, nickname = input().split()
        if t <= s:
            before.add(nickname)
        elif t >= e and t <= q:
            after.add(nickname)

    except:
        break

print(len(before & after))
