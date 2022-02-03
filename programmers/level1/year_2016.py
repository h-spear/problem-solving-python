# https://programmers.co.kr/learn/courses/30/lessons/12901

days_2016 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weeks = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]


def solution(a, b):
    return weeks[(sum(days_2016[: a - 1]) + b - 1) % 7]
