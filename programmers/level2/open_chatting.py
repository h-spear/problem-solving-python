# https://programmers.co.kr/learn/courses/30/lessons/42888


def solution(record):
    nickname = dict()
    history = []
    for _str in record:
        _str = _str.split()
        cmd, _id, name = _str[0], _str[1], _str[-1]
        if cmd == "Enter":
            nickname[_id] = name
        elif cmd == "Leave":
            pass
        elif cmd == "Change":
            nickname[_id] = name
            continue

        history.append((cmd, _id))

    answer = []
    for cmd, _id in history:
        answer.append(
            "{0}님이 {1}".format(nickname[_id], "들어왔습니다." if cmd == "Enter" else "나갔습니다.")
        )
    return answer
