# https://school.programmers.co.kr/learn/courses/30/lessons/155651


def time_to_minutes(time: str):
    splited = time.split(":")
    return int(splited[0]) * 60 + int(splited[1])


def solution(book_time):
    arr = [0] * 2000

    for s, e in book_time:
        arr[time_to_minutes(s)] += 1
        arr[time_to_minutes(e) + 10] -= 1

    answer = 0
    for i in range(1, 2000):
        arr[i] += arr[i - 1]
        answer = max(answer, arr[i])

    return answer
