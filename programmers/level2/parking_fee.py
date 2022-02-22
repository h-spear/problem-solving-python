# https://programmers.co.kr/learn/courses/30/lessons/92341

import math
from collections import defaultdict


def calc_time(start, end):
    sh, sm = map(int, start.split(":"))
    eh, em = map(int, end.split(":"))

    if sh > eh:
        eh += 24

    return eh * 60 + em - sh * 60 - sm


def solution(fees, records):
    parking_time = defaultdict(int)
    base_time, base_fee, unit_time, unit_fee = fees
    park = dict()
    fee_dict = dict()
    answer = []
    for record in records:
        time, num, cmd = record.split()

        if cmd == "IN":
            park[num] = time
        else:
            start_time = park[num]
            use_time = calc_time(start_time, time)
            parking_time[num] += use_time
            print(num, use_time, park[num], time, use_time)
            del park[num]

    for num in park:
        parking_time[num] += calc_time(park[num], "23:59")

    for num, time in parking_time.items():
        if time < base_time:
            fee_dict[num] = base_fee
        else:
            fee_dict[num] = (
                base_fee + math.ceil((time - base_time) / unit_time) * unit_fee
            )

    fee_dict = sorted([(key, val) for key, val in fee_dict.items()])
    answer = [val for _, val in fee_dict]

    return answer
