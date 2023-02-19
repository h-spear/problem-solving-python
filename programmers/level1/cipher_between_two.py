# https://school.programmers.co.kr/learn/courses/30/lessons/155652


def solution(s, skip, index):

    skip_set = set(skip)
    dictionary = {}
    dictionary_rev = [0] * 26
    idx = 0
    for alpha in "abcdefghijklmnopqrstuvwxyz":
        if alpha not in skip_set:
            dictionary[alpha] = idx
            dictionary_rev[idx] = alpha
            idx += 1

    alpha_count = len(dictionary)

    answer = ""

    for char in s:
        new_idx = (dictionary[char] + index) % alpha_count
        answer += dictionary_rev[new_idx]

    return answer
