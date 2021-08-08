def solution(s):
    answer = len(s)
    for step in range(1, len(s) // 2 + 1):
        compressed = ""
        prev = s[0:step]
        cnt = 1
        for i in range(step, len(s), step):
            if prev == s[i : i + step]:
                cnt += 1
            else:
                compressed += str(cnt) + prev if cnt >= 2 else prev
                prev = s[i : i + step]
                cnt = 1
        compressed += str(cnt) + prev if cnt >= 2 else prev
        answer = min(answer, len(compressed))
    return answer
