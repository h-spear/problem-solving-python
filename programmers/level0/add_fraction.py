def gcd(a, b):
    if a % b:
        return gcd(b, a % b)
    else:
        return b


def solution(denum1, num1, denum2, num2):
    denum = denum1 * num2 + denum2 * num1
    num = num1 * num2
    _gcd = gcd(denum, num)
    return [denum // _gcd, num // _gcd]
