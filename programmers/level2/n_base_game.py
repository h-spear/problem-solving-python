# https://programmers.co.kr/learn/courses/30/lessons/17687

hash = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}


def convert_notation(num, x):
    if num == 0:
        return "0"

    result = ""
    while num:
        remainder = num % x
        if remainder < 10:
            result += str(remainder)
        else:
            result += hash[remainder]
        num //= x
    return result[::-1]


def solution(n, t, m, p):
    string = ""
    i = 0
    while len(string) <= m * t + p:
        string += convert_notation(i, n)
        i += 1

    return string[p - 1 : m * t + p - 1 : m]
