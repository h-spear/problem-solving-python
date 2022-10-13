# https://school.programmers.co.kr/learn/courses/30/lessons/17678#


def conv_time_to_minute(time):
    HH, MM = time.split(":")
    return int(HH) * 60 + int(MM)


def conv_minute_to_time(minute):
    return str(minute // 60).zfill(2) + ":" + str(minute % 60).zfill(2)


def solution(n, t, m, timetable):
    buses = [540 + t * i for i in range(n)]
    timetable = [conv_time_to_minute(time) for time in timetable]
    timetable.sort(reverse=True)

    last_bus = 0
    last_bus_crew = None
    for bus in buses:
        temp = []

        for _ in range(m):
            if not timetable or bus < timetable[-1]:
                break
            else:
                temp.append(timetable.pop())

        last_bus = bus
        last_bus_crew = temp

    if len(last_bus_crew) < m:
        return conv_minute_to_time(last_bus)
    else:
        return conv_minute_to_time(last_bus_crew[-1] - 1)
