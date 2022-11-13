# https://school.programmers.co.kr/learn/courses/30/lessons/135807


def get_divisor(num):
    divisor = []
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            divisor.append(i)
            if num // i != i:
                divisor.append(num // i)
    return sorted(divisor, reverse=True)


def gcd(a, b):
    if a % b:
        return gcd(b, a % b)
    else:
        return b


def solution(arrayA, arrayB):
    answer = 0
    gcd_a = arrayA[0]
    gcd_b = arrayB[0]
    for num_a, num_b in zip(arrayA, arrayB):
        gcd_a = gcd(gcd_a, num_a)
        gcd_b = gcd(gcd_b, num_b)

    for num1 in get_divisor(gcd_a):
        for num2 in arrayB:
            if num2 % num1 == 0:
                break
        else:
            answer = num1
            break

    for num1 in get_divisor(gcd_b):
        if num1 < answer:
            break

        for num2 in arrayA:
            if num2 % num1 == 0:
                break
        else:
            answer = num1
            break

    return answer
