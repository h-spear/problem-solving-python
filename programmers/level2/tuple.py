# https://programmers.co.kr/learn/courses/30/lessons/64065

from collections import defaultdict
import re


def solution(s):
    counter = defaultdict(int)
    numbers = list(map(int, re.sub("[\{\}]", "", s).split(",")))
    for number in numbers:
        counter[number] += 1
    return [int(key) for key, val in sorted(counter.items(), key=lambda x: -x[1])]
