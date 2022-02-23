# https://programmers.co.kr/learn/courses/30/lessons/60057


def solution(s):
    if len(s) == 1:
        return 1

    answer = []
    for step in range(1, len(s) // 2 + 1):
        i = 0
        tmp = ""
        while i + step <= len(s):
            j = i + step
            while j + step <= len(s) and s[i : i + step] == s[j : j + step]:
                j += step
            c = ""
            if j - i != step:
                c = str((j - i) // step)

            tmp += c + s[i : i + step]
            i = j
        tmp += s[i:]
        answer.append(tmp)

    answer.sort(key=len)
    return len(answer[0])
