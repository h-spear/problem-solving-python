# https://programmers.co.kr/learn/courses/30/lessons/17683

import re

sharp = {"C#": "c", "D#": "d", "F#": "f", "G#": "g", "A#": "a", "E#": "e"}


def calc_time(start, end):
    sh, sm = map(int, start.split(":"))
    eh, em = map(int, end.split(":"))
    if sh > eh:
        eh += 24
    return (eh * 60 + em) - (sh * 60 + sm)


def convert_sharp_info(string):
    for key, val in sharp.items():
        string = re.sub(key, val, string)
    return string


def failure(pattern):
    table = [0] * len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = table[j - 1]

        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j

        return table


def KMP(string, pattern, table):
    ls = len(string)
    lp = len(pattern)
    j = 0
    for i in range(ls):
        while j > 0 and string[i] != pattern[j]:
            j = table[j - 1]

        if string[i] == pattern[j]:
            if j == lp - 1:
                return True
            j += 1
    return False


def solution(m, musicinfos):
    m = convert_sharp_info(m)
    table = failure(m)
    result = []
    for idx, musicinfo in enumerate(musicinfos):
        start, end, title, info = musicinfo.split(",")
        time = calc_time(start, end)
        info = convert_sharp_info(info)
        if time < len(m):
            continue
        if len(info) < time:
            repeat = (time - 1) // len(info)
            info += info * repeat
        info = info[:time]

        if KMP(info, m, table):
            result.append((time, -idx, title))

    result.sort(reverse=True)
    return result[0][2] if len(result) != 0 else "(None)"
