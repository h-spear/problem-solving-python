# https://programmers.co.kr/learn/courses/30/lessons/92335


def convert_base(num, x) -> str:
    converted = ""
    while num:
        converted += str(num % x)
        num //= x
    return converted[::-1]


def is_prime_number(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def solution(n, k):
    candidates = convert_base(n, k).split("0")
    answer = 0
    for candidate in candidates:
        if candidate == "":
            continue
        if is_prime_number(int(candidate)):
            answer += 1
    return answer
