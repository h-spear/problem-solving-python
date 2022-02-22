# https://programmers.co.kr/learn/courses/30/lessons/49993


def solution(skill, skill_trees):
    answer = 0
    skill += "0"
    for skill_tree in skill_trees:
        i = 0
        for curr in skill_tree:
            if curr == skill[i]:
                i += 1

        if len(set(skill_tree) & set(skill)) == i:
            answer += 1
    return answer
