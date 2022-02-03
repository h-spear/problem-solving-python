# https://programmers.co.kr/learn/courses/30/lessons/81301

import re


def solution(s):
    words = [
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
    for i, word in enumerate(words):
        s = re.sub(word, str(i), s)
    return int(s)
