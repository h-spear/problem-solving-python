# https://programmers.co.kr/learn/courses/30/lessons/12981


def solution(n, words):
    answer = [0, 0]
    last = words[0][-1]
    used = set([words[0]])
    for i, word in enumerate(words):
        if i == 0:
            continue
        if last != word[0] or word in used:
            return [i % n + 1, i // n + 1]
        last = word[-1]
        used.add(word)
    return answer
