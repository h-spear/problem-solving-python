# https://school.programmers.co.kr/learn/courses/30/lessons/120894


def solution(numbers):
    nums = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]

    for i, num in enumerate(nums):
        numbers = numbers.replace(num, str(i))

    return int(numbers)
