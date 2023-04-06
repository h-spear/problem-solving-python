# https://school.programmers.co.kr/learn/courses/30/lessons/178870


def solution(sequence, k):
    n = len(sequence)
    i = 0
    j = 1
    summation = sequence[0]
    minLength = 9876543210
    answer = []

    t = 0
    while j < n:
        if summation > k:
            summation -= sequence[i]
            i += 1
        elif summation < k:
            summation += sequence[j]
            j += 1
        else:
            if minLength > j - i:
                minLength = j - i
                answer = [i, j - 1]
            summation -= sequence[i]
            i += 1

    while i < n:
        if summation == k and minLength > j - i:
            minLength = j - i
            answer = [i, j - 1]
            break

        summation -= sequence[i]
        i += 1

    return answer
