# https://school.programmers.co.kr/learn/courses/30/lessons/150370

YEAR = 28 * 12
MONTH = 28


def date_to_number(date):
    y, m, d = map(int, date.split("."))
    return y * YEAR + m * MONTH + d


def solution(today, terms, privacies):
    mapper = {}
    for term in terms:
        f = term.split()
        mapper[f[0]] = int(f[1]) * 28

    today_date_number = date_to_number(today)

    answer = []
    for idx, privacy in enumerate(privacies):
        date, c = privacy.split()
        expired_date_number = date_to_number(date) + mapper[c]
        if expired_date_number <= today_date_number:
            answer.append(idx + 1)

    return answer
