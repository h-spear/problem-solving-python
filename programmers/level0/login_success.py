# https://school.programmers.co.kr/learn/courses/30/lessons/120883


def solution(id_pw, db):
    tId, tPw = id_pw
    for _id, pw in db:
        if _id != tId:
            continue
        if pw == tPw:
            return "login"
        else:
            return "wrong pw"

    return "fail"
