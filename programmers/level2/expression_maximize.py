from itertools import permutations
from collections import deque


def calc(a, b, op):
    if op == "+":
        return str(int(a) + int(b))
    elif op == "-":
        return str(int(a) - int(b))
    else:
        return str(int(a) * int(b))


def simulate(expression, operator):
    for op in operator:
        stack = []
        while expression:
            x = expression.popleft()
            if x != op:
                stack.append(x)
                continue
            a = stack.pop()
            b = expression.popleft()
            stack.append(calc(a, b, op))
        expression = deque(stack)
    return abs(int(stack[0]))


def solution(expression):
    data = deque(
        expression.replace("+", "|+|")
        .replace("-", "|-|")
        .replace("*", "|*|")
        .split("|")
    )

    result = []
    for prio in permutations(["+", "-", "*"], 3):
        exp = data.copy()
        result.append(simulate(exp, prio))

    return max(result)
