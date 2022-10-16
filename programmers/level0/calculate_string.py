# https://school.programmers.co.kr/learn/courses/30/lessons/120902


def solution(my_string):
    return eval(my_string)


def solution(my_string):
    answer = 0
    oplist = ["+", "-"]
    op = ""
    strings = my_string.split()
    for s in strings:
        if s.isdigit():
            if op == "":
                answer = int(s)
            elif op == "+":
                answer += int(s)
            elif op == "-":
                answer -= int(s)
            op = ""
        else:
            if s in oplist:
                op = s

    return answer
