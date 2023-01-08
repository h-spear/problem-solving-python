# https://school.programmers.co.kr/learn/courses/30/lessons/150368

from itertools import product

g_discount = [10, 20, 30, 40]


def solution(users, emoticons):
    n = len(users)
    m = len(emoticons)
    res = []

    for discount in product(g_discount, repeat=m):
        service_users = 0
        sales_amount = 0

        for dis_per, upperbound in users:
            consumed = 0
            for i in range(m):
                if discount[i] >= dis_per:
                    consumed += (emoticons[i] * (100 - discount[i])) // 100

            if consumed >= upperbound:
                service_users += 1
            else:
                sales_amount += consumed
        res.append((service_users, sales_amount))

    res.sort(key=lambda x: (-x[0], -x[1]))
    return res[0]
