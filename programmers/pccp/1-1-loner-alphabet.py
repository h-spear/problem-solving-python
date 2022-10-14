# https://school.programmers.co.kr/learn/courses/15008/lessons/121683

import re
from collections import Counter


def solution(input_string):
    counter = Counter(input_string)
    candidates = []
    for char, count in counter.items():
        if count <= 1:
            continue
        pattern = char + "*" + char
        if len(re.findall(pattern, input_string)) >= 2:
            candidates.append(char)

    if not candidates:
        return "N"
    return "".join(sorted(candidates))
