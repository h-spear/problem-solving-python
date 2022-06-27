# https://www.acmicpc.net/problem/13171


def powmod(a, x, p):
    if x == 0:
        return 1
    elif x == 1:
        return a

    temp = powmod(a, x // 2, p)
    if x & 1:
        return (temp * temp * a) % p
    else:
        return (temp * temp) % p


p = 1000000007
A = int(input())
x = int(input())
print(powmod(A, x, p))
