# https://programmers.co.kr/learn/courses/30/lessons/17686
# 정규표현식 공부

from functools import cmp_to_key


def split_name(file):
    is_number = False
    head_idx, num_idx = 0, 0
    cnt = 0
    # F15 같은 경우를 처리하기 위함
    file += " "

    for i in range(len(file)):
        if file[i].isdigit() and is_number == False:
            head_idx = i
            is_number = True
            cnt = 1
        if is_number:
            if file[i].isdigit() == False or cnt == 6:
                num_idx = i
                break
            else:
                cnt += 1

    head = file[:head_idx].lower()
    number = file[head_idx:num_idx]
    while number[0] == "0":
        if number == "0":
            break
        number = number[1:]
    return [head, number]


def compare(a, b):
    a_head, a_num = split_name(a)
    b_head, b_num = split_name(b)

    # 1. HEAD 기준 사전 정렬, 대소문자 구분X
    if a_head < b_head:
        return -1
    elif a_head > b_head:
        return 1

    # 2. NUMBER 기준 정렬
    a_num, b_num = int(a_num), int(b_num)
    return a_num - b_num

    # 3. 나머지는 기존 유지


def solution(files):
    return sorted(files, key=cmp_to_key(compare))
