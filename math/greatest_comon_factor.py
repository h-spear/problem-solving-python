# https://www.acmicpc.net/problem/1850


def gcd(a, b):
    if not a % b:
        return b
    else:
        return gcd(b, a % b)


a, b = map(int, input().split())
_gcd = gcd(a, b)
print("1" * _gcd)
