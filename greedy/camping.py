# https://www.acmicpc.net/problem/4796

tc = 0
while 1:
    tc += 1
    l, p, v = map(int, input().split())
    if l == p == v == 0:
        break
    print("Case {}: {}".format(tc, (v // p) * l + min(l, (v % p))))
