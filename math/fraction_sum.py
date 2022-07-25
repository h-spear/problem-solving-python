def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())

n = a1 * b2 + a2 * b1
m = b1 * b2
g = gcd(n, m)

print(n // g, m // g)
