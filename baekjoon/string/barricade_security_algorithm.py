# https://www.acmicpc.net/problem/9322

for tc in range(int(input())):
    n = int(input())
    _hash = dict()
    pk1 = list(input().split())
    pk2 = list(input().split())
    cipher = list(input().split())
    lc = len(cipher)
    for i, str in enumerate(pk1):
        _hash[str] = i

    o = []
    for str in pk2:
        o.append(_hash[str])

    plain = [0] * lc
    for i, x in enumerate(cipher):
        plain[o[i]] = x

    print(" ".join(plain))
