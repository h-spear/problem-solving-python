# https://programmers.co.kr/learn/courses/30/lessons/43165
# 코딩테스트 고득점 Kit : dfs/bfs

answer = 0


def dfs(numbers, target, cur=0, i=0):
    global answer
    if i == len(numbers):
        if cur == target:
            answer += 1
        return

    for sign in [-1, 1]:
        dfs(numbers, target, cur + sign * numbers[i], i + 1)


def solution(numbers, target):
    dfs(numbers, target)
    return answer
