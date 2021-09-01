# Binary Exponetiation (or Exponentiation by squaring)
# a^n = a × a × ... × a = O(logn)


def pow_recursion(C, n):
    if n == 1:
        return C

    x = pow_recursion(C, n // 2)
    if n % 2 == 0:
        return x * x
    else:
        return x * x * C


def pow(C, n):
    res = 1
    while n:
        if n & 1:
            res *= C
        C *= C
        n >>= 1

    return res


print(pow(2, 30))
print(pow_recursion(2, 30))
