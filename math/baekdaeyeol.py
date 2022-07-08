# https://www.acmicpc.net/problem/14490


def gcd(a, b):
    if a % b:
        return gcd(b, a % b)
    else:
        return b


n, m = map(int, input().split(":"))
_gcd = gcd(n, m)
print("{}:{}".format(n // _gcd, m // _gcd))
