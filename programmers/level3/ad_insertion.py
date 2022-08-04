# https://school.programmers.co.kr/learn/courses/30/lessons/72414


def transfer_time_to_sec(time: str) -> int:
    h, m, s = map(int, time.split(":"))
    return h * 3600 + m * 60 + s


def transfer_sec_to_time(sec: int) -> str:
    h = str(sec // 3600).zfill(2)
    sec %= 3600

    m = str(sec // 60).zfill(2)
    sec %= 60

    s = str(sec).zfill(2)

    return ":".join([h, m, s])


def solution(play_time, adv_time, logs):
    play_sec = transfer_time_to_sec(play_time)
    adv_sec = transfer_time_to_sec(adv_time)
    play_per_sec = [0] * (play_sec + 1)
    for log in logs:
        s, e = log.split("-")
        s_sec = transfer_time_to_sec(s)
        e_sec = transfer_time_to_sec(e)

        play_per_sec[s_sec] += 1
        play_per_sec[e_sec] -= 1

    for i in range(1, play_sec + 1):
        play_per_sec[i] += play_per_sec[i - 1]

    curr = sum(play_per_sec[:adv_sec])
    left = 0
    right = adv_sec - 1
    max_length = curr
    start_sec = 0
    while right < play_sec:
        right += 1
        curr += play_per_sec[right]

        curr -= play_per_sec[left]
        left += 1

        if max_length < curr:
            max_length = curr
            start_sec = left

    return transfer_sec_to_time(start_sec)
