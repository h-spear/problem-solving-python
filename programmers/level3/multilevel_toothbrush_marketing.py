# https://school.programmers.co.kr/learn/courses/30/lessons/77486


def solution(enroll, referral, seller, amount):
    graph = {name: None for name in enroll}
    counter = {name: 0 for name in enroll}
    graph["-"] = None

    for name, ref in zip(enroll, referral):
        graph[name] = ref

    def dfs(name, profit):
        if not profit:
            return
        if name == "-":
            return
        dt = int(profit * 0.1)
        adder = profit - dt
        counter[name] += adder
        ref = graph[name]
        dfs(ref, dt)

    for selr, amnt in zip(seller, amount):
        dfs(selr, amnt * 100)

    return [counter[name] for name in enroll]
