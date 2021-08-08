# https://programmers.co.kr/learn/courses/30/lessons/42889


def solution(N, stages):
    answer = []
    data = []
    length = len(stages)

    for stage in range(1, N + 1):
        FailureCount = stages.count(stage)
        if FailureCount != 0:
            data.append((FailureCount / length, stage))
            length -= FailureCount
        else:
            data.append((0, stage))
    data.sort(key=lambda x: (-x[0], x[1]))

    for x in data:
        answer.append(x[1])

    return answer


stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(5, stages))
