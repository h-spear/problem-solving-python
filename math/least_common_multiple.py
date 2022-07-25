# https://www.acmicpc.net/problem/13241


def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


def lcm(a, b):
    return (a * b) // gcd(a, b)


a, b = map(int, input().split())

print(lcm(a, b))
