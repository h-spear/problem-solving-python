# https://programmers.co.kr/learn/courses/30/lessons/72410

import re

def solution(new_id):
    # 1
    new_id = new_id.lower()
    # 2
    new_id = re.sub("[^a-z0-9-_.]", "", new_id)
    # 3, 4
    stack = []
    for x in new_id:
        if len(stack) == 0 and x == ".":
            continue
        if stack and stack[-1] == "." and x == ".":
            continue
        stack.append(x)

    while stack and stack[-1] == ".":
        stack.pop()

    # 5
    if len(stack) == 0:
        stack = ["a"]

    # 6
    if len(stack) >= 16:
        stack = stack[:15]
    while stack and stack[-1] == ".":
        stack.pop()

    # 7
    while len(stack) <= 2:
        stack.append(stack[-1])

    answer = "".join(stack)
    return answer
