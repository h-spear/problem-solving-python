# https://programmers.co.kr/learn/courses/30/lessons/42746
# functools의 cmp_to_key를 사용하여 커스텀한 정렬 기준을 사용할 수 있음

from functools import cmp_to_key


def compare(a, b):
    if int(a + b) < int(b + a):
        return 1  # 0 or 양수 : a, b의 순서를 변경
    return -1  # 음수 : 순서 유지


def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=cmp_to_key(compare))
    answer = "".join(numbers)
    return "0" if answer[0] == "0" else answer
