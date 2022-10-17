# https://school.programmers.co.kr/learn/courses/30/lessons/120878


def gcd(a, b):
    if a % b:
        return gcd(b, a % b)
    else:
        return b


def get_prime_factors(num):
    d = 2
    factors = set()
    while num != 1:
        if num % d == 0:
            factors.add(d)
            num //= d
        else:
            d += 1

    return factors


def solution(a, b):
    b //= gcd(a, b)
    factors = get_prime_factors(b)
    if 2 in factors:
        factors.remove(2)
    if 5 in factors:
        factors.remove(5)
    return 2 if len(factors) else 1
