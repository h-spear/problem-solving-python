# https://school.programmers.co.kr/learn/courses/30/lessons/12904


def is_palindrome(s):
    ls = len(s)
    for i in range(ls):
        if s[i] != s[ls - i - 1]:
            return False
    return True


def solution(s):
    n = len(s)
    answer = 0
    for i in range(n):
        for j in range(i + 1, n + 1):
            ## 효율성 통과
            ## 길이가 이미 현재 answer 값보다 작으면 palindrome을 확인할 필요없음.
            if j - i < answer:
                continue
            if is_palindrome(s[i:j]):
                answer = max(answer, j - i)

    return answer
