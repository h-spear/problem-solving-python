# https://programmers.co.kr/learn/courses/30/lessons/60057


def solution(s):
    answer = len(s)
    for step in range(1, len(s) // 2 + 1):
        compressed = ""
        count = 1
        for i in range(step, len(s) + 1, step):
            if s[i - step : i] == s[i : i + step]:
                count += 1
            else:
                compressed += (
                    str(count) + s[i - step : i] if count >= 2 else s[i - step : i]
                )
                count = 1

        if i >= len(s) - step:
            compressed += s[i:]
        answer = min(answer, len(compressed))

    return answer


print(solution("ababcdcdababcdcd"))
